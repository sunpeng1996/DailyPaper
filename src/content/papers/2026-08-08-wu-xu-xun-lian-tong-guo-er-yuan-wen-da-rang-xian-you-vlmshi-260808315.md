---
title: 'Your VLM Already Knows When: Training-Free Temporal Grounding by Asking Yes
  or No'
title_zh: 无需训练：通过二元问答让现有VLM实现精准时序视频定位
authors:
- Ji Huang
- Barry Devereux
- Hui Wang
affiliations:
- Queen’s University Belfast
arxiv_id: '2608.08315'
url: https://arxiv.org/abs/2608.08315
pdf_url: https://arxiv.org/pdf/2608.08315
published: '2026-08-08'
collected: '2026-08-12'
category: Multimodal
direction: 多模态大模型 · 无训练时序视频定位
tags:
- VLM
- Temporal Grounding
- Training-free
- Binary QA
- Multimodal LLM
one_liner: 将时序定位从时间戳回归改为粗到细二元问答，无需训练即可大幅提升冻结VLM的时序定位效果
practical_value: '- 当LLM/VLM生成数值类结果（如时间戳、价格区间、排序分）置信度高但准确率低时，可将直接生成任务拆分为二元判断排序任务，无需额外训练即可提升效果

  - 做电商短视频商品定位、直播片段选品等跨模态内容检索时，可复用粗到细的二元扫描架构，无需额外时序标注即可快速上线时序定位能力

  - 可复用错误拆解思路：将模型错误拆分为感知能力（由底座决定）和任务接口（可优化）两类，优先优化接口层面问题，大幅降低调优成本'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有VLM可准确识别视频事件，但直接要求输出时间戳完成时序定位时效果极差，Charades-STA数据集上R@0.5最低仅3.8%，且77%-80%的错误预测置信度高，熵基错误检测效果甚至不如随机分类，验证问题出在任务接口而非感知能力。
**方法**：冻结VLM权重，将时间戳回归任务替换为粗到细的二元问答扫描，仅用回答“是/否”的首token概率做排序，无需任何时序监督训练；同时将残留错误拆解为感知轴（由底座能力决定）和几何轴（可通过输出窗口与事件宽度的比值预测）。
**结果**：提出的FV-Action方法在Charades-STA上R@0.5达56.8%，比同底座原生流程提升28-50个百分点；零样本下在TACoS上超过所有经过TVG训练的模型，在ActivityNet Captions、QVHighlights上也显著优于直接预测方案。
