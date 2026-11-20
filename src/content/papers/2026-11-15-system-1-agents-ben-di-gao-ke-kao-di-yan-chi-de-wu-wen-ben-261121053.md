---
title: 'System 1 agents: a method for local, reliable and fast agentic AI'
title_zh: System 1 Agents：本地高可靠低延迟的无文本生成智能体框架
authors:
- Eleftherios Tzanis
- Michail E. Klontzas
affiliations:
- University of Crete
- Karolinska Institute
- University Hospital of Heraklion
arxiv_id: '2611.21053'
url: https://arxiv.org/abs/2611.21053
pdf_url: https://arxiv.org/pdf/2611.21053
published: '2026-11-15'
collected: '2026-11-20'
category: Agent
direction: Agent 工具调用优化 · 零幻觉本地部署
tags:
- Agent
- Tool Calling
- Zero Hallucination
- Local Deployment
- Decision Model
one_liner: 通过多选项决策模型替代LLM文本生成，实现零幻觉、可本地部署的高可靠工具调用智能体
practical_value: '- 工具调用场景可复用「确定性编译器+决策模型」架构替代LLM生成工具调用，彻底解决工具名/参数/值的幻觉问题，适合电商平台内部API调用、商品查询Agent等对正确性要求高的场景

  - 参数填充环节可借鉴从用户query、schema、上下文枚举候选值的策略，无需依赖LLM开放生成，大幅降低推理延迟和算力成本，适合大流量推荐/搜索场景的意图识别、参数补全

  - 决策阈值设计可复用：工具选择、参数填充、能力校验环节均设置置信度阈值，低于阈值直接引导用户补充信息，避免错误猜测，适合电商客服Agent、导购Agent的高容错要求场景

  - 可直接复用开源框架快速搭建业务Agent，支持本地部署避免用户敏感数据泄露，符合电商用户隐私合规要求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent工具调用高度依赖LLM，云LLM会泄露敏感数据不符合医疗、电商等场景的隐私合规要求，本地小LLM幻觉率高，工具调用时的错误参数值会在流程中传导造成隐性错误，推理优化又会大幅提升延迟和算力成本，落地难度大。
### 方法关键点
- 架构分三模块：Agent负责流程控制，完成工具选择、能力校验，置信度低于阈值直接拒绝服务或请求用户补全信息；确定性编译器将工具JSON Schema与用户请求转换为多选项问题，候选值仅来自用户请求、工具Schema、固定规则转换结果，无开放生成；决策模型单次前向传播输出选项概率，全程不生成文本
- 从设计上杜绝幻觉：所有工具、参数名、参数值均来自预设集合，缺失必填参数时用固定模板询问用户，不自动猜测填充
- 开发阶段用编译器Oracle定位问题，仅修改通用规则而非工具专属规则，保证泛化性
### 关键结果
在1952条生物医学请求、157个工具的测试集上，最优System1 Agent工具调用准确率97.0%，参数填充准确率97.0%，全流程正确率93.9%，优于所有18种本地LLM Agent配置（最优LLM全流程正确率91.3%）；零幻觉，远低于LLM 5.5%-19.7%的调用含幻觉值的比例；单请求耗时1.2-10.1s，能耗仅为带推理的LLM的1/3-1/10，可单48GB GPU部署。
### 核心结论
工具调用类Agent无需依赖LLM开放生成，将问题转换为多选项决策任务可同时实现高准确率、零幻觉、低延迟和本地部署。
