---
title: Can Edge-Deployable Vision-Language Models Identify Species?
title_zh: 边缘部署级视觉语言模型的物种识别能力评测
authors:
- William Zhou
- Mayukha Siripuram
- Xiao Yan
- Ziqi Liu
- Yi Ding
affiliations:
- Plano West Senior High School
- Centennial High School
- The University of Texas at Dallas
arxiv_id: '2609.11916'
url: https://arxiv.org/abs/2609.11916
pdf_url: https://arxiv.org/pdf/2609.11916
published: '2026-09-10'
collected: '2026-09-12'
category: Eval
direction: 多模态模型 边缘部署场景能力评测
tags:
- VLM
- Edge Deployment
- Zero-shot Learning
- Hallucination
- Model Evaluation
one_liner: 评测2-8B参数边缘级VLM与专业小模型BioCLIP在物种识别任务的性能与泛化特性
practical_value: '- 垂直领域小模型选型优先看训练数据匹配度而非模型规模，300M参数领域专用模型效果远超2-8B通用VLM，适合电商端侧商品识别、线下门店盘点等低资源边缘场景复用该选型逻辑

  - 跨域性能衰减核心源于图像质量偏移而非模型通用能力缺陷，做户外/低质图像识别类Agent（如线下巡店、快递件识别）时，优先优化输入图像预处理环节而非盲目更换大模型

  - 多模型幻觉率相对排序在不同测试集上完全一致，业务模型选型时可先用小测试集预排幻觉优先级，无需全量测试即可快速筛除高幻觉风险模型，降低评测成本'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
野外相机多部署在无网络的边缘硬件，前沿大模型无法适配，亟需验证2-8B参数可边缘部署VLM的垂直领域专业知识能力，填补该类模型在低质野外图像场景的能力评估空白。

### 方法关键点
选取4款2-8B通用VLM（Qwen3-VL 2B/4B/8B、Gemma3 4B）与300M参数专业物种识别模型BioCLIP对标，在96类物种识别任务上，分别测试干净公开数据集图像与6组野外相机采集低质图像的效果，搭配2组独立采样测试集验证结论鲁棒性。

### 关键结果数字
1. 所有模型野外图像准确率下降9.6~26.6pp，衰减源于图像可读性而非细粒度识别能力缺陷
2. 小参数量BioCLIP准确率比所有测试VLM高33.2~59.2pp，领域训练数据价值远高于模型规模
3. 开放集prompt下5.9~9.6%响应为语法正确但不存在的物种名，不同模型幻觉率相对排序跨测试集完全一致，比单点准确率指标鲁棒性更强
