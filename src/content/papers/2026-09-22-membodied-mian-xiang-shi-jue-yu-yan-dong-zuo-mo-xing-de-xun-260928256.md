---
title: 'MemBodied: Recurrent Associative Memory for Vision-Language-Action Models'
title_zh: MemBodied：面向视觉语言动作模型的循环关联记忆架构
authors:
- Tej Deep Pala
- Navonil Majumder
- Bryce Goh
- Raphael Yee
- Jianfei Yang
- Liming Chen
- Soujanya Poria
affiliations:
- Nanyang Technological University
- Griffin Labs
- École Centrale de Lyon
arxiv_id: '2609.28256'
url: https://arxiv.org/abs/2609.28256
pdf_url: https://arxiv.org/pdf/2609.28256
published: '2026-09-22'
collected: '2026-09-24'
category: Agent
direction: 具身Agent · 高效 episodic 记忆设计
tags:
- Associative Memory
- VLA
- Episodic Memory
- Embodied Agent
- Inference Optimization
one_liner: 提出固定大小双通路关联记忆架构，高效提升VLA模型记忆依赖任务性能
practical_value: '- 长序列用户行为建模的推荐/导购Agent场景，可复用双通路记忆设计：动态关联矩阵存会话内多步交互特征，固定锚点存用户入访初始意图/query，完全避免长上下文膨胀

  - 可迁移gated delta rule记忆更新trick：用可学习的保留门/写入门控制记忆更新比例，无需额外检索模块，参数开销低且避免无用信息覆盖关键特征

  - 记忆读取的专用token注入方式可直接复用：将记忆检索结果注入独立上下文token参与注意力计算，比直接修改attention逻辑效果更好，对原有模型侵入性极低

  - 长horizon决策类Agent任务（电商全链路导购、多步广告投放优化），无需存全量历史上下文，固定大小记忆即可实现比滑动窗口更优的效果，推理延迟降低90%+'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLA模型大多仅基于当前观测生成动作，无法处理依赖历史信息的长horizon任务；直接存储全量历史上下文会导致context长度膨胀、推理latency和显存占用线性上升，滑动窗口方案又容易丢失窗口外的关键历史信息，亟需固定大小、低开销的高效 episodic 记忆架构。
### 方法关键点
- 双通路记忆设计：① 循环关联状态：每层对应1个固定大小的关联矩阵，存储交互历史，采用gated delta rule更新，通过可学习的保留门、写入门控制旧记忆保留比例和新记忆写入强度；② episode锚点：压缩会话初始场景的特征作为固定参考，避免早期细节被反复更新覆盖。
- 因果读写逻辑：先基于当前状态读取记忆生成动作，动作执行后结合观测到的环境反馈异步写入记忆，保证因果性，无需额外记忆损失，仅通过原始任务目标端到端训练。
- 低侵入记忆注入：读取的记忆结果投影后加到专用记忆token中参与自注意力，不修改原有模型的attention逻辑。
### 关键实验结果
在5个记忆依赖的RMBench任务上，成功率为无记忆π0策略的7.81倍、原生循环记忆的2.98倍，比最强基线NativeMEM高1.3倍，新增参数仅为其1/10，推理latency低91.9%；LIBERO-Long长序列任务上比无记忆策略高5.4pp，全观测任务平均性能基本持平。
### 核心结论
固定大小的结构化关联记忆完全可以替代膨胀的长上下文，实现更优的长序列决策性能，同时兼顾推理效率。
