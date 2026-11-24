---
title: 'Routing Collapse in Multimodal Mixture-of-Experts: Cross-Modal Conditioning
  Restores Expert Diversity Without Improving Accuracy'
title_zh: 多模态MoE路由坍塌研究：跨模态修复专家多样性但无精度增益
authors:
- Syed Hussamuddin
- Mubashra Fayyaz
affiliations:
- FAST National University of Computer and Emerging Sciences
arxiv_id: '2611.28725'
url: https://arxiv.org/abs/2611.28725
pdf_url: https://arxiv.org/pdf/2611.28725
published: '2026-11-21'
collected: '2026-11-24'
category: Training
direction: MoE训练 · 路由坍塌问题研究
tags:
- MoE
- Multimodal
- Routing Collapse
- Training Stability
- Model Evaluation
one_liner: 证实多模态MoE中跨模态融合可修复路由坍塌，但路由健康与任务性能无绑定关系
practical_value: '- 做多模态MoE推荐/广告模型时，不要盲目以路由熵、专家利用率为优化目标，这类指标提升不一定带来点击率、转化率等业务指标增益，避免无效优化

  - 小数据量场景下使用MoE架构需谨慎，路由坍塌是常态，分散训练信号到多专家反而可能浪费算力，建议先做大单expert模型再考虑拆分

  - 做模型对比实验时必须跑多组随机种子，同配置下模型效果可能有10%+的波动，避免把随机误差当成架构增益，误导业务迭代决策

  - 若确实需要提升MoE专家利用率，跨模态注意力预处理输入是可行trick，无需额外负载均衡损失即可提升路由熵2倍以上'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
MoE架构被广泛应用于多模态任务，其性能增益常被归因于专家分治特性，但小数据场景下的路由坍塌问题很少被直接度量，过往研究默认专家利用率提升对应任务性能提升，缺乏严格对照验证。

## 方法关键点
- 固定7专家MoE头结构，仅调整模态融合方式：对照组用可学习标量门融合文本、语音、动作捕捉三模态嵌入，实验组先做全连接pairwise跨模态注意力再融合输入到MoE头
- 未添加任何辅助负载均衡损失，还原真实场景下MoE的原生路由行为
- 用归一化路由熵、有效专家数量化路由健康度，控制6组随机种子排除随机波动干扰

## 关键结果
实验在IEMOCAP四分类情感数据集上开展：
- 对照组路由熵仅0.241，平均有效专家数1.88，出现严重坍塌，个别运行仅1.53个专家生效，5/7的专家为惰性参数
- 实验组路由熵提升2.23倍到0.537，有效专家数提升到3.25，实现了按情感类别差异化路由
- 两组加权准确率无统计显著性差异（66.51% vs 67.79%，p=0.646），同配置下不同种子的准确率波动最高可达13个百分点

## 核心结论
小数据场景下MoE的路由健康度与任务性能完全解耦，修复路由坍塌的干预措施不一定能带来实际收益，单组种子的实验结果不具备统计可靠性
