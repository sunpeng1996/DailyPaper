---
title: 'dLoop: Looped Diffusion Language Models via Recurrent Latent Refinement'
title_zh: dLoop：基于循环隐层精炼的扩散语言模型
authors:
- Handa Li
- Pengxiang Li
- Mingyu Cao
- Xilu Wang
- Li Shen
- Da Li
- Lu Yin
affiliations:
- University of Surrey
- The Hong Kong Polytechnic University
- Sun Yat-sen University
- University of York
- Shenzhen University of Advanced Technology
arxiv_id: '2611.26275'
url: https://arxiv.org/abs/2611.26275
pdf_url: https://arxiv.org/pdf/2611.26275
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 扩散大语言模型 · 解码效率优化
tags:
- Diffusion LLM
- Looped Transformer
- Latent Refinement
- Parallel Decoding
- Efficient Inference
one_liner: 将预训练扩散语言模型重构为三段架构，通过循环隐层计算提升解码精度与并行度
practical_value: '- 业务中使用扩散类大模型生成推荐文案、广告素材、搜索联想词时，可复用Prelude-Loop-Coda三段拆分方案，仅微调中间共享Loop
  Block即可提升生成准确率，无需全模型重训

  - 低延迟并行生成场景可参考预提交隐层计算思路，无需通过训练强行拉高token置信度，仅在推理阶段增加少量循环计算即可提升每步提交token的可靠性，减少错误上下文累积

  - 多轮Agent思考链优化可借鉴循环块的锚定融合机制，将初始Query表征作为固定锚点结合每轮思考结果，避免循环计算时的状态漂移，提升推理稳定性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
扩散语言模型（DLM）支持并行生成，但每步仅能提交少量置信度足够的token，现有加速方法仅优化置信度学习或提交策略，单次前向传播无法充分融合prompt、已提交token和未提交位置的信息，导致提交时部分预测表征不足，仅靠调整提交策略无法从根源提升预测质量。
### 方法关键点
- 将预训练LLaDA模型拆分为三段架构：Prelude（前15层编码输入）、参数共享Loop Block（16-21层循环计算）、Coda（后10层输出logits）
- 每次额外循环时以Prelude输出为固定锚点，通过带谱约束的融合函数结合上一轮Loop Block输出，避免循环过程中的状态漂移
- 训练时为不同样本分配0~3次循环深度，用标准掩码交叉熵损失微调，无需额外添加置信度相关损失项
- 解码时采用滑动窗口+最低提交数量约束，优先提交置信度高于阈值的token，避免生成停滞
### 关键实验
在GSM8K、MATH、MBPP、HumanEval四个基准上对比Fast-dLLM、dParallel、d3LLM等SOTA方法，dLoop在所有基准上取得最高或并列最高准确率，其中GSM8K准确率达76.3%，MBPP达42.2%；调整循环计算成本后的TPF（每前向传播生成token数）全面优于Fast-dLLM，仅d3LLM的TPF更高但准确率低于dLoop，无方法能在准确率和TPF两个指标上同时超过dLoop。
### 核心结论
预提交阶段的隐层计算可以替代训练阶段的置信度强制损失，成为DLM解码加速的独立新路径。
