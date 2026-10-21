---
title: 'CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?'
title_zh: CoEvo-RSI：模型-Harness协同进化的双向历史继承框架
authors:
- Jiaqi Su
- Guibin Zhang
- Jie-Jing Shao
- Cong Pang
- Tiankuo Yao
- Ivor Tsang
- Haiyan Yin
- Shuicheng Yan
affiliations:
- National University of Singapore
- Agency for Science, Technology and Research (A*STAR)
- SenseTime Group Inc.
arxiv_id: '2610.25078'
url: https://arxiv.org/abs/2610.25078
pdf_url: https://arxiv.org/pdf/2610.25078
published: '2026-10-17'
collected: '2026-10-21'
category: Agent
direction: Agent自进化 · 模型-Harness协同优化
tags:
- RSI
- Co-evolution
- Agent
- Model-Harness
- Self-Improvement
one_liner: 提出双向历史继承的RSI框架，解决脑体失配问题，9B小模型性能追平大模型
practical_value: '- 垂直场景Agent迭代可复用TIMR指标快速诊断模型与工具链/执行工作流的接口适配问题，无需全量评估即可定位脑体失配，降低排查成本

  - 维护垂直领域历史Harness（提示词、工具、工作流）和模型checkpoint归档库，迭代时无需从最新版本启动，配对筛选适配最优的初始组合，减少微调工作量

  - 小模型垂直化训练可复用「拒绝采样合格轨迹 + SFT」的低成本方案，配合双向继承的协同进化流程，性能可追平大模型，推理成本降低1~2个数量级'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
模型-Harness协同进化是当前递归自提升（RSI）Agent的主流范式，但普遍存在被忽略的「脑体失配」问题：进化后的Harness（执行支架，含工具、工作流、接口等）要求的行为模型未习得，或Harness限制了模型已有的能力，导致协同进化效果受限，过往方法仅迭代最新的模型-Harness组合，浪费了历史有效经验。
### 方法关键点
- 搭建统一进化归档库，存储所有历史Harness设计、模型checkpoint、执行轨迹、效果数据，支持全链路追溯
- 元Agent协调双向历史继承：Harness侧基于当前执行反馈从归档选最优历史设计迭代，模型侧针对新Harness的要求，选择或通过TIES-Merging合并历史checkpoint，配对生成候选组合
- 引入轻量诊断指标TIMR（轮次接口失配率），快速筛选接口适配的模型-Harness对，降低评估成本
- 选中的候选组合生成轨迹后，仅用拒绝采样的合格轨迹做SFT微调，验证达标后进入下一轮，所有执行结果回写归档库
### 关键实验
覆盖3个垂直场景：多Agent故障归因、角色感知Text2SQL、智能家居指令跟随，对比基线含大模型直接调用、仅Harness进化、仅模型训练、其他协同进化方案。核心结果：基于Qwen3.5-9B的CoEvo-RSI在TraceElephant故障归因数据集上超过DeepSeek-V4-Pro 14.16%的Agent准确率，在HomeBench VM智能家居任务上超过GLM-5.3 4.90%的成功率，推理成本比最优基线低22~38倍。
### 核心结论
垂直领域Agent优化无需盲目堆大模型，通过模型与执行支架的双向对齐，小模型即可获得追平大模型的效果，同时大幅降低推理成本
