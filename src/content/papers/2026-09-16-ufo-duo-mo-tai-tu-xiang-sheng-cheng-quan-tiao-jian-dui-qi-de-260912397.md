---
title: 'UFO: Chain-of-Evaluation for Omni-Condition Alignment in Multi-Modal Image
  Generation'
title_zh: UFO：多模态图像生成全条件对齐的链式评估方法
authors:
- Danning Zhang
- Yijing Lin
- Shuhan Zhuang
- Mengqi Huang
- Shaojin Wu
- Shancheng Fang
- Zhendong Mao
affiliations:
- University of Science and Technology of China
- Shenzhen University
- Institute of Artificial Intelligence
- Independent Researcher
arxiv_id: '2609.12397'
url: https://arxiv.org/abs/2609.12397
pdf_url: https://arxiv.org/pdf/2609.12397
published: '2026-09-16'
collected: '2026-09-18'
category: Eval
direction: 多模态生成 · 对齐评估框架
tags:
- Multi-modal Generation
- Chain-of-Evaluation
- Alignment Evaluation
- Benchmark
- MLLM
one_liner: 提出原子化链式评估范式UFO，大幅提升多模态生成全条件对齐评估与人类偏好的相关性
practical_value: '- 电商营销素材/定制化商品图生成场景可复用原子化链式评估思路，将复杂多条件对齐评估拆解为独立可验证的原子单元，替代原有孤立单条件评估，提升评估结果与用户偏好的一致性

  - 多模态Agent任务（如文案配图Agent、个性化内容生成Agent）可借鉴分类型调用专用验证工具的设计，针对不同属性的评估单元选择匹配的验证逻辑，降低评估误差

  - 内部生成模型效果评测可参考UFO-Bench的构建思路，覆盖多模态条件交互的多种场景，避免评测集偏置导致的效果误判'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态图像生成的对齐评估仅孤立校验单模态条件，不符合多条件同时满足的生成目标，与人工判断一致性差，成为生成模型落地的核心瓶颈。
### 方法关键点
提出UFO统一评估框架，采用原子化链式评估范式：1）将全条件对齐任务拆解为细粒度、解耦的Atomic Evaluation Units（AEUs），按模态相关性分类；2）针对不同类型AEU分别调用通用或专用功能接口完成精准校验。同时推出UFO-Bench基准数据集，覆盖文本、视觉条件多种交互场景，可全面评估定制化生成模型性能。
### 关键结果
与人类评估偏好的相关性平均提升15.25%，为当前SOTA多条件对齐评估方案
