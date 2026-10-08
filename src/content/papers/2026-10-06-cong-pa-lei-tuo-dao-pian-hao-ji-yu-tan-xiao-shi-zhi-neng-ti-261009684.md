---
title: 'From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic
  Policy Discovery'
title_zh: 从帕累托到偏好：基于摊销式智能体策略发现的个性化测试时缩放
authors:
- Xinglin Wang
- Zishen Liu
- Tong Zheng
- Shaoxiong Feng
- Peiwen Yuan
- Yiwei Li
- Jiayi Shi
- Yueqi Zhang
- Chuyi Tan
- Ji Zhang
affiliations:
- Beijing Institute of Technology
- Xiaohongshu Inc
arxiv_id: '2610.09684'
url: https://arxiv.org/abs/2610.09684
pdf_url: https://arxiv.org/pdf/2610.09684
published: '2026-10-06'
collected: '2026-10-08'
category: Agent
direction: Agent 个性化测试时缩放策略优化
tags:
- Test-Time Scaling
- Agentic Discovery
- Policy Reuse
- Personalized Inference
- LLM Reasoning
one_liner: 针对LLM测试时缩放多维度用户需求，提出PersonTTS提升需求联合满足率并降低发现开销
practical_value: '- 针对多约束（推荐/广告推理的 latency、成本、准确率联合要求）的个性化策略优化，可复用「需求匹配的相似场景策略初始化+蒸馏经验引导迭代」架构，避免从零搜索，降低调优成本

  - 做Agent自动发现工作流/策略时，可基于离线回放池预存全量推理轨迹，候选策略评估无需重复调用LLM，仅通过回放即可完成，大幅降低策略搜索的token成本和时间开销

  - 多目标优化无需局限于二维帕累托前沿，直接以联合满足率为目标函数端到端优化，对广告要点击率、成本、ecpm同时达标的多约束业务场景适配性更强

  - 跨场景/用户的策略复用可搭配目标侧轻量评估校准，无需完全重新搜索即可在新场景拿到不错效果，适合千人千面的推理资源调度场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Test-time scaling（TTS）仅单独优化准确率-成本或准确率-延迟的二维帕累托前沿，无法满足用户对准确率、延迟、推理成本的联合多维需求；为每个新用户需求单独搜索TTS策略的开销极高（单轮搜索可达39.9美元、160分钟），亟需能复用历史经验的高效个性化TTS方案。

### 方法关键点
- 提出PersonTTS摊销式智能体策略发现框架，目标最大化用户多约束联合满足率（JSR），策略动作空间覆盖模型路由、推理宽深度、剪枝、停止等全量TTS控制逻辑
- 构建策略经验库，基于标准化后的需求向量相似度检索历史最优策略作为初始化，降低冷启动开销
- 从历史策略发现轨迹中蒸馏得到固定Guide，引导LLM discovery agent生成候选策略，避免重复试错
- 所有候选策略基于预构建的离线回放池做目标需求侧评估，无需额外调用任务LLM，保证评估效率和公平性

### 关键结果
在AIME、HMMT数学推理数据集上基于6款Qwen3模型测试，对比AutoTTS、ASC、ParallelProbe等基线：无经验复用的PersonTTS在AIME目标用户集上JSR达85.57%，远超最优基线AutoTTS（β=1.0）的35.58%；加入跨用户经验复用后，JSR进一步提升至96.57%，同时策略发现时间降低46%、成本降低36%；经验库规模从20扩容到100时，发现集JSR持续提升，但跨问题泛化不一定单调增长，需做置信度校准。

### 核心结论
多约束业务场景下，直接优化联合满足率比单独优化二维帕累托前沿的业务价值更高，经验复用能大幅降低个性化策略的发现成本。
