---
title: 'Steerable by Design: Conditional Pretraining for Robust Control of Language
  Models'
title_zh: 内置可控性：基于条件预训练的大语言模型鲁棒控制方法
authors:
- Henry Castillo
- Yanchen Liu
- Claudio Mayrink Verdun
- Dylan Hadfield-Menell
affiliations:
- Cambridge-Boston Alignment Initiative
- Massachusetts Institute of Technology
- Harvard University
arxiv_id: '2611.32199'
url: https://arxiv.org/abs/2611.32199
pdf_url: https://arxiv.org/pdf/2611.32199
published: '2026-11-23'
collected: '2026-11-26'
category: Training
direction: 大语言模型 · 可控预训练
tags:
- Conditional Pretraining
- Steerable LLM
- Sparse Autoencoder
- Adversarial Robustness
- Control Channel
one_liner: 提出带独立语义控制通道的条件预训练框架，生成模型的鲁棒转向能力远超同规模基线
practical_value: '- 业务Agent/LLM应用可参考独立控制通道设计，将系统prompt、安全规则、品牌约束等与用户输入上下文分离，大幅降低prompt注入、上下文对齐漂移风险，比如电商客服Agent可将话术规范放在独立通道，避免用户恶意诱导偏离规则

  - 可复用SAE特征提取+条件预训练思路做领域可控生成，比如电商商品文案生成时，将「营销属性」「合规属性」「类目特征」作为独立控制信号注入，生成结果既能贴合上下文又能严格符合约束，避免LoRA微调后约束失效的问题

  - 数据拼接增强trick可直接复用：预训练时按15%概率随机替换文档片段，降低上下文可预测性，强迫模型依赖控制信号，适合小参数领域模型的可控性训练，减少后续对齐工作量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM的对齐与控制均在预训练后完成，仅占总训练token的1%左右，指令与数据共用输入通道，极易出现越狱、上下文对齐漂移、微调后安全属性失效等问题，后对齐的猫鼠游戏成本极高且无法根治鲁棒性缺陷。

### 方法关键点
- 架构上采用独立encoder处理语义控制信号，decoder通过单向交叉注意力读取控制通道，文本token流无法回写控制通道，从底层实现指令与数据分离
- 控制信号基于SAE稀疏特征构建，经过滤、聚类得到844个高质量可解释语义单元，正负激活分别表示生成需包含/排除对应属性
- 预训练阶段加入数据拼接增强，15%概率随机替换文档片段，降低上下文可预测性，强迫模型依赖控制信号；训练目标结合next token预测与下一段语义特征预测的辅助损失
- 支持自然语言转控制信号，通过语义检索+轻量残差校正实现单句描述到控制向量的映射，无需为每个新控制目标单独微调

### 关键结果
- MANCELLE-3B仅用同规模基线5%的训练token，steering强度与Qwen2.5-3B-Instruct、SmolLM3-3B的prompt steering相当
- 黑盒GEPA攻击下，基线模型的prompt steering仅保留19%~26%的控制效果，MANCELLE-3B保留88%~92%；RL红队攻击下，基线模型95%的控制目标被突破，MANCELLE-3B仅被突破1~2个
- 白盒软prompt攻击下，MANCELLE-3B仍保留81%~92%的控制效果，远高于基线最高60%的保留率

最值得记住的一句话：要实现远高于现有方案的可控行为鲁棒性，更具扩展性的方案是在预训练阶段就注入对齐约束，而非仅在训练完成后做表层对齐。
