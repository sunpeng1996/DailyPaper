---
title: 'HarnessEval-W: Agentifying the Evaluation of Visual Worlds'
title_zh: HarnessEval-W：面向视觉世界模型的Agent化评估框架
authors:
- Weiliang Chen
- Haowen Sun
- Jun Gao
- Jiawei Chi
- Hanyang Wang
- Qiyu Dai
- Yihao Li
- Hao Li
- Jingnan Gao
- Yi-Hsin Hung
arxiv_id: '2608.16859'
url: https://arxiv.org/abs/2608.16859
pdf_url: https://arxiv.org/pdf/2608.16859
published: '2026-08-16'
collected: '2026-08-18'
category: Eval
direction: Agent化评估 · 世界模型基准
tags:
- Agentic Evaluation
- World Model
- Benchmark
- Multi-Agent Pipeline
- Visual Generation
one_liner: 提出层级Agent化的视觉世界模型评估框架，输出可溯源推理链，对齐人类偏好
practical_value: '- 可复用层级Agent评估架构：将复杂评估任务拆分为父Agent路由+子Agent专项验证的结构，可迁移到生成式推荐的文案/素材质量评估、推荐结果合理性校验等场景，解决固定指标无法覆盖复杂语义判断的问题

  - 可借鉴评估可溯源设计：每个评分绑定证据树和完整推理链，可直接复用到电商广告素材预审、用户反馈归因等业务，能快速定位低质内容的具体问题点，减少人工审核成本

  - 可参考自动化case构造流程：通过分类采样+Agent生成+校验的流水线构造评估用例，可用于生成推荐系统的AB测用例、搜索相关性测试集，大幅降低人工标注成本

  - 结论复用：不同评估维度的相关性结论可指导业务评估体系设计，比如生成内容的渲染质量和物理合理性几乎无关，需分设独立评估模块'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有世界模型评估多为固定规则的黑盒指标，无法解释评分依据，也难以适配不同场景下物理因果、时序一致性、世界状态演变的复杂校验需求，和人类判断偏差大、结果不可追溯，无法为模型优化提供明确指引。

### 方法关键点
- 框架设计：采用层级Agent工作流，顶层父Agent根据评估case的上下文（初始图像、动作Prompt、评估目标）路由到对应评估技能，每个技能再拆分为可量化子问题，分配给专用子Agent执行校验
- 评估维度：围绕世界模型3个核心能力设8个细分评估轴：观测质量（渲染质量、物理合理性）、过渡正确性（探索过渡、意图过渡、物理过渡）、世界持久性（漂移抗性、重访一致性、离屏演变）
- 用例构造：通过结构化场景分类采样+Agent自动生成+有效性校验的流水线，构造330个覆盖多场景、多交互类型的评估用例，降低人工标注成本与偏差
- 输出设计：每个评估结果对应完整证据树，记录所有子Agent的评分、推理依据和工具调用过程，完全可溯源

### 关键实验
在330个评估用例上测试18个主流世界模型，和人类偏好的斯皮尔曼相关性在意图过渡任务达0.93、物理过渡任务达0.87；对比现有基准WBench，物理过渡评估的pairwise准确率从31.9%提升到71.7%，平局率从52.2%降至1.8%，三次重复实验的评分稳定性是WBench的4.9倍。

最值得记住的一句话：未来的基准不再是固定规则的黑盒指标，而是能自适应拆解问题、组装工具、推理每一个评估case的智能评估器。
