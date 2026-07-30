---
title: 'LaP-Forensics: Latent-Pixel Consistency Guided Multimodal Reasoning for Deepfake
  Detection'
title_zh: LaP-Forensics：隐层-像素一致性引导的多模态深度伪造检测
authors:
- Can Wang
- Yuhao Wang
- Yushe Cao
- Canran Xiao
- Fei Shen
affiliations:
- The Hong Kong Polytechnic University
- University College London
- Tsinghua University
- Sun Yat-sen University
- National University of Singapore
arxiv_id: '2607.25962'
url: https://arxiv.org/abs/2607.25962
pdf_url: https://arxiv.org/pdf/2607.25962
published: '2026-07-28'
collected: '2026-07-30'
category: Multimodal
direction: 多模态伪造检测 · DDIM残差校验
tags:
- Multimodal Reasoning
- Deepfake Detection
- DDIM
- Stable Diffusion
- GRPO
one_liner: 提出融合DDIM重建残差与RGB语义的多模态深度伪造检测框架，支持伪影定位与可解释文本分析
practical_value: '- 电商内容审核场景可复用DDIM重建残差校验思路，检测AI生成的虚假商品图、营销素材，降低漏判率

  - 结构化「位置-内容-原因」多模态输出范式可迁移到违规内容归因场景，输出可解释的审核判定依据

  - GRPO多目标加权奖励的调优思路，可用于需同时满足分类准确率+输出结构化合规性的多任务优化'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前SOTA生成模型产出的图像几乎无明显视觉伪影，仅依赖表层外观特征的深度伪造检测器性能与可解释性大幅下降。
### 方法关键点
1. 基于冻结的Stable Diffusion DDIM反演重建模块生成固定参考，计算输入图与参考的残差图衡量局部一致性
2. 独立投影层分别编码RGB图像与残差图，经Where-What-Why结构化推理模块同时输出文本分析结果与伪影掩码
3. 先完成监督微调，再通过GRPO强化学习优化，奖励函数融合掩码交并比、输出结构一致性、证据参考一致性三类指标
4. 独立分类头融合RGB与DDIM残差特征输出图像级真伪判定
### 关键结果
在UniversalFakeDetect数据集实现跨生成器检测效果，在SynthScars基准上伪影定位性能达到SOTA水平。
