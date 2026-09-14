---
title: 'CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation'
title_zh: CMA-OT：面向舞蹈到音乐生成的分层专家监督框架
authors:
- Jinting Wang
- Chenxing Li
- Dong Yu
- Li Liu
affiliations:
- HKUST(GZ)
- Tencent
arxiv_id: '2609.13118'
url: https://arxiv.org/abs/2609.13118
pdf_url: https://arxiv.org/pdf/2609.13118
published: '2026-09-11'
collected: '2026-09-14'
category: Multimodal
direction: 跨模态生成 · 分层专家监督
tags:
- Cross-Modal Generation
- Curriculum Learning
- Optimal Transport
- Hierarchical Supervision
- Representation Alignment
one_liner: 提出融合课程引导多尺度对齐与尺度感知最优传输的框架，实现舞蹈到音乐生成SOTA
practical_value: '- 分层专家监督思路可直接迁移到电商短视频自动配乐、直播背景音生成等多模态内容生产场景，降低内容制作成本

  - 课程引导的渐进式多尺度知识蒸馏策略，可复用在文本生成商品图、用户行为生成推荐文案等稀疏输入到稠密输出的任务，缓解语义gap

  - 尺度感知最优传输软对齐机制，可用于解决序列匹配的时序错位问题，比如用户行为序列与item属性序列对齐、多轮对话与推荐结果匹配'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
舞蹈到音乐生成任务存在固有语义鸿沟：稀疏的舞蹈节奏、风格等输入 cues 无法匹配音乐生成所需的稠密结构、配器、动态表达信息，现有方法仅监督最终音频输出，导致生成音乐乐感弱、结构连贯性差。
### 方法关键点
1. 引入外部预训练音乐专家提供分层监督信号，对齐生成器隐层特征，弥合跨模态语义gap
2. 采用课程引导多尺度学习策略，渐进式将专家音乐知识迁移到生成器，保障训练稳定性与表示学习效果
3. 提出尺度感知最优传输对齐机制，建模不同层级专家表示与生成器隐特征的软对应，解决时序错配下的细粒度对齐问题
### 关键结果
在两个公开数据集上达到SOTA，节奏同步性、感知质量、整体生成效果均显著优于现有基线方法
