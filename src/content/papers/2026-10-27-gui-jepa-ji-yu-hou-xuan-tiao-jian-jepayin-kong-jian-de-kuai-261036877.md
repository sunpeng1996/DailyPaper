---
title: 'GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile
  GUI Agents'
title_zh: GUI-JEPA：基于候选条件JEPA隐空间的快速移动GUI智能体策略
authors:
- Bingchao Wang
- Yongcheng Jing
- Shunyu Liu
- Chengyu Wang
- Jun Huang
- Jie Yang
- Wei Liu
- Dacheng Tao
affiliations:
- Shanghai Jiao Tong University
- Nanyang Technological University
- Alibaba Cloud Computing
arxiv_id: '2610.36877'
url: https://arxiv.org/abs/2610.36877
pdf_url: https://arxiv.org/pdf/2610.36877
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: GUI智能体 · 低延迟推理优化
tags:
- GUI-Agent
- JEPA
- Latent-Scoring
- Efficient-Inference
- VLM-Optimization
one_liner: 基于JEPA隐空间批量打分替代VLM解码，GUI智能体提速2.8-4倍，精度保留86-92%
practical_value: '- 低延迟Agent场景可直接复用「候选枚举+隐空间批量打分」替代VLM token-by-token生成的架构，适合电商导购、端侧自动操作类场景，实测延迟降低2.8-4倍，精度仅损失8-14%

  - 复用“JEPA编码器冻结+轻量预测器对齐决策目标”的训练范式，无需做JEPA动态预训练，随机初始化预测器效果与动态预训练版本相当，大幅降低训练成本

  - 多模态候选排序可参考「视觉隐态结构打分+MiniLM文本匹配」的组合方案，平衡视觉语义理解和文本匹配精度，适合商品点击、按钮交互等电商GUI场景

  - 高流量服务可复用置信度路由策略：低置信度请求路由至大模型，高置信度用小模型服务，在精度损失可控的前提下大幅降低服务成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有移动GUI Agent普遍依赖7B+规模VLM逐token生成动作，推理延迟达200ms以上，显存占用超15GB，即使是候选打分方案也需要保留大模型在链路中，无法满足端侧部署、高并发交互的需求，尤其电商导购、自动操作类场景对低延迟、低资源占用要求极高，亟需轻量高效的决策架构。

### 方法关键点
- 预训练：用189K无标注GUI截图预训练JEPA ViT-L编码器，学习GUI通用视觉表征，预训练完成后编码器完全冻结，下游训练无需更新主干
- 无解码器决策：从accessibility树枚举所有可执行动作作为候选集，用39.9M残差预测器将全局屏幕隐态转换为每个候选的条件隐态，单批次完成所有候选处理，全程无token生成
- 混合打分：结构头计算候选隐态与目标指令的余弦相似度得分，叠加33M MiniLM交叉编码器的文本匹配分，最终取最高得分候选作为输出
- 训练优化：仅训练预测器、打分头和文本匹配器，用列表式交叉熵优化，无需JEPA动态预训练，随机初始化预测器效果与动态预训练版本相当

### 关键结果
在AndroidControl数据集上测试，与同输入、同GPU的Qwen2.5-VL-7B LoRA微调Agent对比：GUI-JEPA参数量仅为后者的6%，推理速度快2.8-4.0倍，GPU显存占用仅为1/4.6-1/6.4，分布内精度达到7B模型的86-92%；新增两个轻量文本排序器可额外提升3.8-4.1个OOD精度点。

> 最值得记住的结论：面向结构化候选的决策场景，用「隐空间批量打分」替代大模型逐token生成，可实现用1/10的参数量、1/4的延迟保留85%以上的精度
