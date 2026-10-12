---
title: Can machines reason non-verbally?
title_zh: 《机器可以进行非语言推理吗？》
authors:
- Shaheer U. Saeed
- Zion Tse
- Gregory Slabaugh
- Daniel C. Alexander
- Yipeng Hu
affiliations:
- Queen Mary University of London
- University College London
arxiv_id: '2610.13925'
url: https://arxiv.org/abs/2610.13925
pdf_url: https://arxiv.org/pdf/2610.13925
published: '2026-10-09'
collected: '2026-10-12'
category: Reasoning
direction: 视觉非语言推理通用框架研究
tags:
- Non-verbal Reasoning
- GenVerOpt
- Computer Vision
- Medical Imaging
- Visual Reasoning
one_liner: 提出融合生成、验证、优化的GenVerOpt框架，突破现有模型视觉非语言推理性能瓶颈
practical_value: '- 可借鉴「生成-验证-迭代优化」的pipeline设计，用于生成式推荐的候选结果纠错/迭代打磨，比如AI生成商品详情页、个性化推荐文案的后处理优化

  - 单样本优化思路可迁移至多模态推荐场景的小样本/冷启动任务，无需全量重训即可适配单条内容/商品的个性化匹配需求

  - 非语言推理框架可复用至多模态Agent的视觉交互任务，比如电商导购Agent识别用户上传的实物图、穿搭图中的模糊需求并迭代匹配商品'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前ChatGPT、Gemini等先进系统在语言逻辑推理上表现优秀，但在需要视觉非语言推理的任务（如抽象模式补全、模糊感兴趣区域划分）上性能受限；且视觉推理中间步骤隐式，无明确验证方法，是当前机器智能的核心短板之一。

### 方法关键点
提出GenVerOpt通用框架，将生成、验证、优化统一为推理流水线：先生成候选解，再验证正确性，最后迭代优化，实现单样本级别优化，无需仅依赖训练阶段捕捉的数据集级趋势，流程模仿人类思考时的多方案假设-评估-迭代逻辑。

### 关键结果
在多领域任务上性能超越现有系统：抽象IQ谜题测试超过人类水平，前列腺癌分割性能持平临床医生，肝血管重建效果超过领域专家，肿瘤边界对齐任务优于现有SOTA方法。
