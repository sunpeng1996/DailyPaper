---
title: Learning When Diffusion Language Models Should Regenerate
title_zh: 面向扩散语言模型的块级再生决策轻量验证器DiVR
authors:
- Minhae Oh
- Jeonghye Kim
- Jinwoo Koo
- Yeongoon Kim
- Jimin Seo
- Minsik Seol
- Jungwoo Lee
affiliations:
- Seoul National University
- KAIST
arxiv_id: '2611.17320'
url: https://arxiv.org/abs/2611.17320
pdf_url: https://arxiv.org/pdf/2611.17320
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 扩散大语言模型 · 推理优化与自验证
tags:
- Diffusion LLM
- LoRA
- Verifier
- Inference Optimization
- Reasoning
one_liner: 共享生成器权重的轻量验证器，以远低于搜索基线的成本提升扩散LLM推理准确率
practical_value: '- 生成式推荐/电商文案生成场景若使用扩散LLM，可复用DiVR块级校验逻辑：无需逐token纠错，直接对低置信度块整体重生成，修复上下文关联错误，成本远低于全采样重排

  - 轻量验证器设计可直接迁移：复用生成器backbone加LoRA+简单MLP头做校验，仅新增1%参数，无需token级标注，只用最终结果对错训练，适配业务侧标注成本有限的场景

  - 生成质量校验思路可复用：隐藏状态比token置信度更能反映最终结果正确性，业务侧做生成内容质检时可优先用中间层隐藏状态做探针，准确率显著高于输出层置信度

  - 块级优化的成本控制思路可复用：阈值θ可直接作为效果/算力的tradeoff旋钮，业务侧可根据预算灵活调整，无需修改整体解码流程'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有扩散语言模型（MDLM）的重生成策略依赖固定调度规则、token置信度或外部大模型校验，要么修复效率低，要么推理成本过高；诊断实验发现单独修正错误token时，周围上下文会维持原有错误模式，修复成功率不足10%，亟需更高效的重生成决策机制。
### 方法关键点
- 轻量验证器设计：共享生成器的frozen backbone，仅新增LoRA适配层+2层MLP打分头，新增参数量仅占backbone的1%
- 弱监督训练：仅用生成序列最终结果的对错标注，不需要token级标注，训练目标融合二分类损失（判断序列最终是否正确）和pairwise排序损失（正确序列打分高于错误序列）
- 块级再生解码：每生成固定长度的块后对当前部分序列打分，得分低于阈值θ则整体重生成当前块，保留打分最高的候选，无需定位具体错误token
### 关键结果
在LLaDA-8B、Dream-7B等3个主流扩散LLM上测试，覆盖GSM8K、MATH、HumanEval等5个数学、代码推理基准：
- 对SFT后的LLaDA-8B-Base，平均准确率从35.3%提升至43.4%，仅需1.9~3.5×贪心解码成本；同等效果下，比SR-SMC、Prism等搜索基线节省30%~60%算力
- 具备跨任务、跨模型迁移能力：在GSM8K上训练的验证器可直接提升MATH、Countdown等未见过的任务效果，无需重新训练
### 核心结论
扩散语言模型的错误修正不需要精准定位单个错误token，对上下文关联的块整体重生成，配合仅需结果监督的轻量验证器决策，是性价比远高于搜索基线的优化方案
