---
title: A report-grounded vision-language foundation model for colonoscopy from 280000
  routine reports
title_zh: 基于28万份常规报告的结肠镜视觉语言基础模型
authors:
- Jia Yu
- Yan Zhu
- Yili He
- Zilong Wang
- Xinyang Jiang
- Peiyao Fu
- Ruijie Yang
- Tianyi Chen
- Siyuan Li
- Zhihua Wang
affiliations:
- 复旦大学
- 浙江大学
- 曼彻斯特大学
- 帝国理工学院
- 微软亚洲研究院
arxiv_id: '2607.28466'
url: https://arxiv.org/abs/2607.28466
pdf_url: https://arxiv.org/pdf/2607.28466
published: '2026-07-30'
collected: '2026-08-02'
category: Other
direction: 医疗多模态基础模型 弱监督数据对齐
tags:
- Vision-Language Model
- Weak Supervision
- Foundation Model
- Contrastive Learning
- Medical AI
one_liner: 从弱关联结肠镜常规报告中恢复病灶级图文对，训练出性能更优的专用视觉语言基础模型EndoCLIP
practical_value: '- 弱监督细粒度标注思路可迁移：当业务只有全局标签（如用户全会话行为、商品整页评论）无单样本标注时，可通过匹配规则恢复细粒度样本-文本对做训练，大幅降低标注成本

  - 垂直领域小模型优化方案：基于通用预训练模型用领域内高质量细粒度配对数据微调，性能即可超过通用/泛垂直领域模型的零样本/线性探测效果

  - 自然语言定义任务可降低多任务适配成本：无需为每个下游任务单独标注，用自然语言描述任务目标即可实现零样本适配，提升业务迭代效率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
结肠镜场景视觉语言模型落地受限，常规报告仅做全局流程总结，未与单帧图像绑定，临床发现与对应图像仅弱关联，缺乏高质量细粒度标注。
### 方法关键点
从280476份常规结肠镜记录中逐步恢复出125756组病灶级图文对，基于对比学习训练结肠镜专用视觉语言基础模型EndoCLIP。
### 关键结果数字
1. 在病灶级图文检索、结构化报告生成、6项多中心临床分类任务的零样本/线性探针设置下，性能全面优于通用和生物医学领域VLM
2. 良恶性分类盲测中，EndoCLIP线性探针性能接近12名参与测试的内镜医师专家水平
