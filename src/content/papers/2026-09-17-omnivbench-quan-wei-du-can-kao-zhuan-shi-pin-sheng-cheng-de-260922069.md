---
title: 'OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video
  Generation'
title_zh: OmniVBench：全维度参考转视频生成的评测基准与大规模数据集
authors:
- Wenxue Li
- Peiyan Guan
- Haoyang Jiang
- Junxian Cai
- Hualuo Liu
- Chunjie Zhang
- Chong Guan
- Songlian Li
- Taiyi Wu
- Yongjian Yu
affiliations:
- Online Video BU, Tencent
- The Hong Kong University of Science and Technology (Guangzhou)
arxiv_id: '2609.22069'
url: https://arxiv.org/abs/2609.22069
pdf_url: https://arxiv.org/pdf/2609.22069
published: '2026-09-17'
collected: '2026-09-21'
category: Multimodal
direction: 多模态视频生成 · 评测基准与数据集
tags:
- Reference-to-Video
- Benchmark
- Multimodal Dataset
- Evaluation
- Generative AI
one_liner: 推出覆盖7类任务的全维度R2V生成评测基准与34万样本工业级训练数据集
practical_value: '- 电商带货短视频生成场景可复用其细粒度因子对齐评估逻辑，校验商品特征、运镜、品牌风格等维度的保真性，避免生成内容偏离营销需求

  - 34万标注的工业级R2V数据集可直接用于微调带货视频生成模型，大幅降低自有数据采集标注成本

  - 可复用其多参考组合的任务构建pipeline，快速构造同时参考商品图、爆款视频动效、品牌风格的定制化营销视频训练数据'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有Reference-to-Video（R2V）生成基准覆盖参考类型有限，评估仅关注整体一致性，忽略参考因子的保留、解耦与路由效果，同时高质量全维度R2V训练数据构建成本高、资源稀缺。
### 方法关键点
1. 推出OmniVBench评测基准，覆盖内容、运动、风格、结构、叙事、多参考等7类任务族、18个细粒度任务
2. 设计因子接地评估范式，配套12172条case专属校验项，细粒度评估参考因子的保真度、解耦效果与指令对齐度
3. 开源Omni-R2V工业级数据集，基于专业视频语料构建34万条标注训练样本，提供可扩展的参考-目标对构造流程
### 关键结果
对主流开源/闭源R2V模型的评测显示，各模型在不同任务族、评估维度均存在明显性能gap，现有R2V技术仍有较大优化空间。
