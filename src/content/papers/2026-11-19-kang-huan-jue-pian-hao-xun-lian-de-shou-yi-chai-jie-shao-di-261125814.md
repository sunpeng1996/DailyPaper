---
title: What Does Anti-Hallucination Training Buy? Saying Less, Cheap Pruning, and
  the Rest
title_zh: 《抗幻觉偏好训练的收益拆解：少生成、低成本剪枝与剩余价值》
authors:
- Lingkai Bu
- Qian Gao
affiliations:
- 算力网络与信息安全教育部重点实验室
- 山东省计算中心（国家超级计算济南中心）
- 齐鲁工业大学（山东省科学院）
arxiv_id: '2611.25814'
url: https://arxiv.org/abs/2611.25814
pdf_url: https://arxiv.org/pdf/2611.25814
published: '2026-11-19'
collected: '2026-11-20'
category: Training
direction: 多模态大模型 · 抗幻觉训练收益拆解
tags:
- Hallucination-Mitigation
- Preference-Training
- Multimodal-LLM
- Low-cost-Probe
- DPO
one_liner: 拆解多模态LLM抗幻觉训练收益，证实70%以上非精简收益可被低成本轻量探针复现
practical_value: '- 做电商商品图文生成、卖点文案生成等场景的抗幻觉优化时，优先上线轻量后处理探针+召回匹配基线，无需直接全量SFT/DPO，可大幅降低落地成本

  - 偏好训练标注环节，可采用CLIP、简单特征逻辑回归等低成本标注源替代部分人工标注，能覆盖70%以上的ground truth标注收益，降本效果显著

  - 评估抗幻觉优化效果时必须加入召回匹配的「少说话」对照基线，避免将生成内容变短带来的幻觉降低误判为算法实际收益'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多模态LLM的抗幻觉偏好训练普遍以CHAIR分数下降为核心指标，但存在明显混淆变量：生成内容越短幻觉天然越少，行业既没有拆分训练的真实收益构成，也不清楚是否可用更低成本的方案实现同等抗幻觉效果。
### 方法关键点
- 设计匹配召回的收益拆解协议，将抗幻觉训练的收益拆为三部分：「少说话」（位置匹配随机删除即可实现）、低成本剪枝（轻量探针可复现）、剩余价值
- 低成本探针仅用500张标注图训练的逻辑回归，特征仅含表层统计、COCO类别先验、模型token log-probability三类，训练后全程冻结
- 提出标注源定价方法：以匹配召回下的收益占比，量化低成本标注源相对ground truth标注的效果差距
### 关键实验
- 测试8个公开LLaVA-1.5-7B抗幻觉方法，7/8在COCO、8/8在AMBER、6/8在Object HalBench上，探针可复现2/3以上的非精简收益
- 低成本标注源收益：探针标注、CLIP标注分别可恢复Qwen2.5-VL上ground truth DPO 70%、87%的非精简收益，均优于长度匹配随机标注
- 基础模型加探针在相同召回下，8/9的LLaVA-1.5系统在COCO上优于直接截断生成内容
### 核心结论
抗幻觉优化不要上来就堆训练资源，先验证轻量后处理+召回匹配基线的上限，可节省大量研发和算力成本。
