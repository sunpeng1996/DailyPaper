---
title: 'TerraVis: Towards Evaluation of World-Grounded Visual Consistency in Text-to-Image
  Generation via MLLM Workflows'
title_zh: TerraVis：基于MLLM工作流的文生图真实世界视觉一致性评估框架
authors:
- Shuai Fu
- Jing Gu
- Jian Zhou
- Zicheng Duan
- Gengze Zhou
- Qi Wu
affiliations:
- Adelaide University AIML
- xAI
- Responsible AI Research Centre
arxiv_id: '2610.02959'
url: https://arxiv.org/abs/2610.02959
pdf_url: https://arxiv.org/pdf/2610.02959
published: '2026-10-01'
collected: '2026-10-09'
category: Eval
direction: 多模态大模型 · 生成内容一致性评估
tags:
- MLLM
- Text-to-Image
- Evaluation
- Visual Consistency
- Generative AI
one_liner: 提出分级检测常识错误的文生图评估框架，与人类判断相关性优于现有指标
practical_value: '- 电商AI生成商品图质检可复用其对象/交互/场景三级错误分类体系，快速过滤违背常识的低质生成内容

  - 生成式推荐的图文内容质检可迁移其多阶段MLLM评估架构，先做准入过滤再细粒度打标，降低评估成本

  - AIGC生成质量评估可将世界一致性作为独立补充维度，填补现有美学、图文对齐指标的覆盖盲区'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有文生图评估指标仅覆盖保真度、美学、图文对齐维度，无法识别违背真实世界常识的错误（如畸形物体、不符合物理规则的交互、空间关系矛盾等），这类错误会严重影响生成内容的业务可用性。
### 方法关键点
1. 定义覆盖对象级、交互级、场景级共18类常识错误的结构化分类体系；
2. 采用多阶段MLLM评估流程：先判断图像是否符合评估准入条件，再逐类检测错误并划分轻重等级，最终输出整体世界一致性得分。
### 关键结果
在2个通用基准、多款开源/闭源文生图模型上，TerraVis与人类对世界一致性的判断相关性为现有指标最高；传统指标表现优秀的模型仍存在大量常识一致性错误。
