---
title: 'What the Loss Curve Misses: FP4 Pretraining Slows the Acquisition of Rare
  Facts'
title_zh: 损失曲线无法反映：FP4预训练降低稀有事实学习效率
authors:
- Chang Lu
- Mengjiao Zhang
affiliations:
- Independent Researcher
arxiv_id: '2611.12832'
url: https://arxiv.org/abs/2611.12832
pdf_url: https://arxiv.org/pdf/2611.12832
published: '2026-11-09'
collected: '2026-11-10'
category: Training
direction: 大模型低精度训练 · 稀有知识学习
tags:
- Low-Precision Training
- FP4
- Fact Acquisition
- Pretraining
- Adam Optimization
one_liner: 证实FP4低精度预训练在验证损失接近时，需多20%~50%曝光才能达到同等稀有事实召回效果
practical_value: '- 做垂域大模型（电商商品知识库/广告创意生成/Agent记忆模型）预训练时，不能仅用验证loss评估低精度训练效果，需额外增加长尾实体/稀有规则的召回测试，避免长尾知识学习不足导致业务效果下降

  - 若使用FP4预训练支撑RAG/Agent的内置记忆模块，需将长尾事实的训练曝光量提升20%~50%，才能达到和BF16训练同等的知识记忆效果

  - 优化低精度训练配方时，优先降低反向传播的梯度噪声（比如反向传播用FP8精度），比单纯调整学习率更能提升稀有知识的学习效率，且验证loss变化极小，落地成本低

  - 可复用论文的梯度统计诊断方法，仅用BF16 checkpoint的梯度数据就能快速排序不同低精度配方的知识学习成本，无需全量训练测试'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前低精度预训练（尤其是FP4）普遍仅通过验证loss评估效果，但token平均的loss对长尾稀有事实权重极低，无法反映模型对长尾知识的学习能力，而电商/广告/推荐场景的长尾实体、稀有用户偏好、垂直领域规则恰恰是业务效果的核心瓶颈，亟需明确低精度训练对稀有知识学习的实际影响。
### 方法关键点
- 构造曝光次数可控的合成传记数据集，每个事实的曝光次数从1到256次不等，单独训练或混入通用网页文本训练，控制唯一变量为矩阵乘法精度（BF16/FP8/NVFP4/MXFP4）
- 提出**曝光乘数**指标：低精度模型达到和BF16基线同等稀有事实召回时，所需的事实曝光次数比值，直接量化学习效率差距
- 拆分前向/反向传播量化、注入可控梯度噪声，定位Adam优化器下梯度噪声对学习效率的影响机制
### 关键结果
- 合成数据集上，NVFP4验证损失仅比BF16高0.5%，但需1.32倍曝光才能达到同等召回，损失匹配时仍需1.2倍曝光
- 自然文本混合场景下，NVFP4验证损失仅高2%，但需1.52倍曝光才能达到同等召回，损失匹配时仍需1.22倍曝光
- 仅量化反向传播时，损失几乎无变化，但曝光乘数仍达1.13倍，该效应来自梯度噪声导致的Adam更新信噪比下降，调大学习率无法修复
### 最值得记住的结论
低精度训练的验证损失达标不代表长尾知识学习达标，评估低精度训练配方必须加入长尾事实的召回指标
