---
title: 'Agentic LongLive: Asynchronous Agentic Memory for Long Video Generation'
title_zh: Agentic LongLive：异步智能体记忆驱动的实时长视频生成框架
authors:
- Shaoteng Liu
- Shuai Yang
- Wei Huang
- Luozhou Wang
- Song Han
- Yukang Chen
affiliations:
- NVIDIA
- MIT
- CUHK
arxiv_id: '2611.34907'
url: https://arxiv.org/abs/2611.34907
pdf_url: https://arxiv.org/pdf/2611.34907
published: '2026-11-24'
collected: '2026-11-26'
category: Agent
direction: 智能体长时记忆 · 实时流系统优化
tags:
- Agentic_Memory
- Asynchronous_Computing
- Long_Video_Generation
- RL_Policy
- Attention_Sink
- KV_Cache
one_liner: 提出异步离环智能体记忆架构，在不拖慢实时生成的前提下大幅提升长视频实体与场景一致性
practical_value: '- 异步计算架构可直接复用在实时推荐/搜索/Agent交互系统，将用户画像更新、候选集预计算、记忆推理等耗时操作放在独立进程异步执行，完全不阻塞请求响应路径，实现零额外延迟

  - 离环记忆设计可迁移到生成式推荐/导购Agent系统，仅从可信输入（用户显式行为、查询词、官方商品库）更新记忆，不读取生成的内容，避免错误属性、错误回复被写入记忆导致级联传播

  - RL优化的记忆筛选策略可用于长会话用户建模，用小参数LoRA模型学习高价值记忆筛选规则，在有限的KV cache槽位、召回候选槽位中优先保留对后续交互增益最高的用户特征、商品/内容候选

  - 双模态记忆设计可复用在多模态推荐/直播导购场景，文本实体卡片保证属性准确性，参考图像保证视觉一致性，解决长交互流程中商品形象、用户偏好漂移的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
实时自回归视频生成依赖KV cache存储历史帧，会遗忘长周期的人物、物品、场景特征，且生成错误会级联传播；现有多镜头视频生成智能体需要提前读取全量脚本、等待规划完成、支持重绘错误镜头，完全无法适配实时流生成零等待、无回滚、未来输入未知的核心要求。
### 方法关键点
- 异步记忆架构：智能体运行在独立GPU上，在上一镜头生成阶段预计算下一镜头的记忆，通过辅助GPU提前将记忆预填充到生成器的attention sink中，完全隐藏智能体计算延迟，生成器无任何等待
- 离环双层记忆：智能体仅读取已暴露的提示词，不读取生成的视频内容，避免错误回灌；第一层为实体记忆，存储每个角色/物品/场景的文本状态和图像特征，第二层为合成的全局记忆图G和镜头记忆图M，预填充为KV cache的sink注入生成器
- RL记忆规划：用GRPO训练加LoRA的8B小模型作为记忆规划器，奖励函数结合下游视频效果校准，自动选择需要保留和更新的实体，效果与35B大模型相当
- 轻量runtime逻辑：提示词到达时仅做场景匹配召回预填充记忆，同时为提示词中出现的实体追加属性文本卡片，强化一致性
### 关键结果
在自建LongStory-Online基准（25个故事共857个镜头）上测试：对比基线LongLive-2.0，持久状态准确率提升26.3pp，主角身份一致性提升44.9pp，重访场景一致性提升40.4pp，仅增加1%生成耗时；8×B200上端到端帧率达34.3FPS，超过实时24FPS要求，14分钟长视频的身份一致性和画质无明显衰减；效果可迁移到MiniMax-H3系列生成器，主角身份一致性从60%左右提升至97%以上。
> 最值得记住：只要将非核心路径的计算全部异步化、预计算化，智能体完全可以在不拖慢实时系统的前提下提供长时记忆能力，无需牺牲实时性换长周期一致性。
