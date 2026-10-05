---
title: 'Corrupted but Correct: Why Vision-Language Models Lie to Themselves Internally'
title_zh: 被扰动仍正确：视觉语言模型内部「自欺」现象的机制解析
authors:
- Arun Josephraj Arokiaraj
- Zekun Wu
- Adriano Koshiyama
affiliations:
- University College London
- Holistic AI
arxiv_id: '2610.03445'
url: https://arxiv.org/abs/2610.03445
pdf_url: https://arxiv.org/pdf/2610.03445
published: '2026-10-02'
collected: '2026-10-05'
category: Multimodal
direction: 多模态大模型 · 对抗鲁棒性机制解析
tags:
- VLM
- Adversarial Robustness
- Autoregressive Model
- Mechanistic Interpretability
- Train-Inference Gap
one_liner: 揭示自回归VLM训练推理差距的机制，明确其对抗鲁棒性由语言解码器决定
practical_value: '- 搭建多模态Agent（如商品图文理解、直播内容审核）的对抗防御体系时，优先优化LLM解码器侧的先验校验逻辑，无需在视觉encoder侧投入过多冗余成本

  - 部署多模态生成/理解服务时，可在首个自回归生成步骤插入校验探针，基于合并隐层状态的线性探针提前识别被扰动输入，AUC可达0.858

  - 训练多模态推荐相关VLM时，不要仅依赖teacher-forced损失判断训练效果，必须补充自由生成的推理侧指标，避免训练推理gap导致线上效果失真'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
自回归VLM存在诡异的训练推理gap：对抗扰动可将固定目标caption的teacher-forced训练损失降到接近0，但模型自由生成时仍输出原正确描述，背后机制不明确，严重影响落地系统的鲁棒性与可信度。
### 方法关键点
以Qwen2.5-VL-7B-Instruct为研究对象，对200张COCO held-out图片执行两阶段PGD攻击，结合logit lens、28层LLM decoder的target-token rank追踪、合并隐层状态线性探针开展机制解析。
### 关键结果数字
1. 像素级特征（含CNN鲁棒性文献中的纹理攻击性度量）对攻击成功率几乎无预测能力，最高相关系数r=-0.050，岭回归R²=0.069；
2. 训练推理gap集中在首个自回归步骤，目标token在152064词表中的排名固定为3488，零方差；
3. 视觉编码器会同等程度扰动所有图片表征，最终结果由LLM解码器仲裁：易感图片放大扰动信号，抗性图片主动抑制至低于干净图基线，rank-biserial r=0.579，p<0.001；
4. 合并隐层状态线性探针可区分两种结果，AUC=0.858。
