---
title: 'WithEveryone: Unified Planning and Identity Grounding for Group Image Generation'
title_zh: WithEveryone：面向群体图像生成的统一规划与身份对齐框架
authors:
- Hengyuan Xu
- Qixun Wang
- Yiji Cheng
- Miles Yang
- Zhao Zhong
- Wei Cheng
- Xingjun Ma
- Yu-gang Jiang
affiliations:
- Fudan University
- Hunyuan, Tencent
- The University of Hong Kong
arxiv_id: '2608.20336'
url: https://arxiv.org/abs/2608.20336
pdf_url: https://arxiv.org/pdf/2608.20336
published: '2026-08-19'
collected: '2026-08-21'
category: Multimodal
direction: 多模态生成 · 身份保留群体图像生成
tags:
- Identity-Preserving Generation
- Group Image Generation
- Layout Grounding
- Token Injection
- Multimodal Generation
one_liner: 提出带布局对齐身份损失的统一框架，支持最多10个指定身份的高保真群体图像生成
practical_value: '- 电商/广告多人营销素材生成场景可直接复用身份-布局绑定逻辑，解决指定KOL/模特同框生成时的身份错乱、复制粘贴伪影问题

  - 多主体生成任务的训练阶段可参考Layout-Grounded ID Loss设计，用标注区域直接监督对应主体生成，替代不稳定的embedding匹配校验逻辑

  - 生成多主体可控内容时可提前输出结构化布局计划作为中间控制条件，大幅提升多主体生成的可控性与准确率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有身份保留图像生成在多指定人物同框场景表现极差：不仅存在身份绑定错乱、人脸相似度低问题，训练阶段依赖embedding匹配校验预测人脸的方案稳定性差，生成结果还易出现复制粘贴伪影，最多支持的同框身份数量少。
### 方法关键点
1. 统一框架支持最多10个参考身份的群体图像生成，将每个选中身份编码为可寻址token输入模型
2. 先预测结构化身份-布局绑定计划，包含人物区域、姿态等信息，渲染为视觉条件后再输入生成模块
3. 核心损失Layout-Grounded ID Loss直接用标注人脸区域监督对应身份生成，规避embedding匹配的不稳定性
4. 新增ID Representation Forcing模块，在图像合成前预训练每个身份的预测表征
### 关键结果
在身份不相交基准集上，人脸相似度从GPT-Image-2的0.462提升至0.499，复制粘贴伪影率从0.169降至0.055；指定身份覆盖率达97.3%，身份重复率仅2.8%
