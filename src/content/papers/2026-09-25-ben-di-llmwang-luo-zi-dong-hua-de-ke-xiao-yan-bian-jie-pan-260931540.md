---
title: Can You Check That? The Checkability Boundary for Local LLM Network Automation
title_zh: 本地LLM网络自动化的可校验边界判定与落地框架
authors:
- Maleeha Masood
- Momina Nofal
affiliations:
- University of Illinois Urbana-Champaign
- Independent Researcher
arxiv_id: '2609.31540'
url: https://arxiv.org/abs/2609.31540
pdf_url: https://arxiv.org/pdf/2609.31540
published: '2026-09-25'
collected: '2026-09-28'
category: LLM
direction: 本地SLM部署 · 任务可校验边界判定
tags:
- SLM
- Intrinsic Check
- Local LLM Deployment
- Model Escalation
- Network Automation
one_liner: 提出基于任务固有校验的本地SLM推理准入方案，仅16%左右输入需升级至云端大模型
practical_value: '- 可复用「多SLM生成候选+任务确定性校验过滤+低置信升级大模型」的分层推理架构，降低电商敏感业务（如用户隐私数据处理、订单自动审核）的数据泄露风险，同时压缩大模型调用成本

  - 快速构造业务专属低成本校验规则：比如商品文案生成校验必须包含指定SPU属性、推荐理由生成校验不出现未授权竞品词、Agent工具调用结果校验参数合法，无需额外调用LLM即可过滤80%以上错误输出

  - 多SLM集成时仅需少量开发样例离线计算各模型任务权重，用加权投票聚合输出，无需微调即可提升本地模型基线准确率，适合边缘端低资源推理场景'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
前沿大模型落地网络自动化场景需上传敏感生产配置、拓扑、日志数据，推理成本高昂；本地SLM虽规避了数据泄露与成本问题，但输出错误率高无法直接使用，亟需一套轻量准入规则筛选可靠输出，仅将难例升级至云端大模型。
### 方法关键点
- 定义intrinsic check：仅依赖输入、输出与本地状态的确定性必要条件校验，无需ground truth、额外LLM或远程接口，不通过直接淘汰候选，通过仅代表满足必要正确性条件，单独统计假阳率（FAR）衡量校验可靠性。
- 设计Touchstone三层pipeline：离线阶段用100-150条开发样例计算7款1-8B SLM的任务专属权重；在线阶段多SLM生成候选，经任务专属校验过滤后加权投票聚合结果，置信度低于0.6的输入升级至前沿大模型，升级时附带校验错误信息作为修复提示。
- 针对不同任务定制低开销校验规则：冲突检测用规则提取<地点,前缀>对判断一致性，意图翻译校验输出实体全来自输入、规则数量匹配需求，日志解析校验模板可还原原始日志，代码生成用单元测试做执行校验。
### 关键实验
在4类结构化网络任务（冲突检测、意图翻译、日志解析、路由代码生成）与无校验规则的知识问答数据集TeleQnA上测试，对比全量调用GPT-5.5的baseline：
- 冲突检测任务端到端精度98.6%，仅16%输入需升级，假阳率为0；意图翻译精度93.8%，升级率17%，假阳率5.6%，接近云端精度的同时大幅降低敏感数据流出率。
- 无固有校验的知识问答任务精度仅78.2%，无法匹配云端84.2%的精度，验证校验规则是本地SLM部署的核心前提。
### 核心结论
本地SLM部署的核心问题不是“模型是否足够强”，而是“任务是否足够容易校验”，支持低开销精确校验的任务适合优先本地化，其余请求升级云端。
