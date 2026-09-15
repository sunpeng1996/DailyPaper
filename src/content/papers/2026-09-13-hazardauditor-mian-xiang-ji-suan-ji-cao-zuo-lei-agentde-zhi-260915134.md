---
title: 'HazardAuditor: From Executable Threats to Safer Computer-Use Agents'
title_zh: HazardAuditor：面向计算机操作类Agent的执行侧安全防护框架
authors:
- Yunhao Feng
- Ruixiao Lin
- Ming Wen
- Yanming Guo
- Xingjun Ma
- Yutao Wu
- Xinhao Deng
- Shouling Ji
affiliations:
- Ant Group
- Zhejiang University
- Fudan University
- Hunan Institute of Advanced Technology
- Deakin University
arxiv_id: '2609.15134'
url: https://arxiv.org/abs/2609.15134
pdf_url: https://arxiv.org/pdf/2609.15134
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 运行时安全审计与防护
tags:
- Agent_Safety
- Guard_Model
- Policy_Optimization
- LLM_Agent
- Runtime_Audit
one_liner: 提出基于执行轨迹的Agent安全审计框架，搭配GuardPO优化，跨异构Agent检测精度最高升16.5pp
practical_value: '- 电商/运营Agent安全检测可复用异构轨迹归一化方案：将不同Agent框架的用户输入、工具调用、环境返回统一为标准事件Schema，一套安全模型适配多Agent业务线，减少重复开发

  - 训练带解释的生成式审核/安全模型时可直接复用GuardPO优化思路：以单条样本的决策为优化单元，对长解释和短判决做区域归一化，避免长解释主导梯度，低召回审核场景下可提升判决准确率

  - 业务上线可参考快慢双路部署架构：生成式Guard做最终判决，冻结主干加轻量MLP头做前置预筛，平衡审核准确率和 latency，适配推荐/广告的高吞吐请求场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent安全防护方案要么仅检测静态内容，无法识别执行过程中产生的组合风险；要么仅做安全评估，输出的非标准化日志无法直接用于训练通用安全模型，且常规SFT训练生成式Guard时，token级优化会让长解释的梯度权重远高于最终判决，导致核心判决准确率偏低。

### 方法关键点
- 可执行安全基础设施：适配Claude Code、Codex、Hermes、OpenClaw四类异构Agent，将交互日志统一归一化为包含用户输入、Agent输出、工具调用、环境观测的标准事件表示，标注区分「仅观测到风险内容」和「实际发起风险操作」两类样本，降低误判
- Guard Policy Optimization（GuardPO）：将安全判决作为优化单元，给单条样本的所有token分配相同的序列级优势，分别归一化解释区域和判决区域的损失，消除解释长度对梯度的影响，保证最终判决是优化核心
- 两段式训练：先做带解释监督的SFT冷启动，再用GuardPO微调，最终输出包含可审计分析和二分类安全判决的结果

### 关键实验
在CUA-EXEC跨Agent基准上，对比最强基线BraveGuard，精度最高提升16.5pp；在AgentHazard、ASSE-Safety等4个公开Agent安全基准上均达到SOTA，跨数据集最低F1达88.3%，比最优基线高7.6pp；基于Qwen3Guard-8B初始化的模型，8B参数即可超过GPT-5.2、Claude Sonnet 4.6等闭源大模型的安全检测效果。

### 核心结论
Agent安全防护不能只依赖静态内容检测，必须基于实际执行行为训练，且优化目标要和最终的业务判决单元对齐
