---
title: 'HeadEdit: Calibrating Language Model Behavior Through the Frozen Unembedding
  Matrix'
title_zh: HeadEdit：基于冻结未嵌入矩阵的大语言模型行为校准方法
authors:
- Zirui He
- Haiyan Zhao
- Jingyu Hu
- Yinghao Wu
- Chenxi Yuan
- Yingcong Li
- Yandong Bai
- Mengnan Du
affiliations:
- New Jersey Institute of Technology
- University of Bristol
- Kuaishou Technology
- The Chinese University of Hong Kong, Shenzhen
arxiv_id: '2610.01170'
url: https://arxiv.org/abs/2610.01170
pdf_url: https://arxiv.org/pdf/2610.01170
published: '2026-10-01'
collected: '2026-10-02'
category: LLM
direction: LLM对齐 · 无梯度行为校准
tags:
- LLM Alignment
- Gradient-free
- Unembedding Matrix
- Behavior Calibration
- Low-rank Subspace
one_liner: 无梯度无需参数更新，通过未嵌入层低秩行为子空间实现LLM行为自适应校准
practical_value: '- 电商Agent工具调用校准：可复用HeadEdit的低秩子空间方法，仅用少量正负样例对即可降低工具过度调用、错误拒绝正常请求的问题，无需微调模型，工程成本极低

  - 生成式推荐输出校准：针对LLM生成推荐文案、商品推荐时的幻觉/过度安全拒绝问题，可通过构建对应正负生成对提取行为子空间，在推理阶段动态调整logit，不影响模型通用能力

  - 大模型部署优化：HeadEdit的推理开销可忽略，无需修改模型参数，可直接叠加在已完成LoRA微调的模型上进一步提升效果，无需重新提取子空间或调参'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM对齐方法存在明显局限：梯度类方法（如DPO）需针对每个目标重新优化，激活steering需手动选择干预层且会影响后续计算，解码期对齐依赖启发式搜索或辅助模型，增加推理成本。且对齐后的模型仍存在过度拒绝无害请求、不必要工具调用、事实性谄媚等残留行为错误，而相关行为信息实际已经编码在模型最终隐状态中，只是未嵌入层无法将其转换为正确的token得分，存在表征到输出的gap。
### 方法关键点
- 无需梯度、无需更新任何模型参数，仅用少量`<prompt, 正例输出, 负例输出>`三元组，通过SVD从正负输出的隐状态差值中提取低秩行为子空间
- 推理阶段将当前预未嵌入隐状态投影到该子空间，通过冻结的未嵌入矩阵生成全词表logit校正量，校正量随prompt动态变化，无需手动指定目标token
- 等价于对未嵌入层做低秩修改，无需实际修改权重，仅在推理期做轻量矩阵运算
### 关键实验
在3个模型族（Qwen3-4B、Gemma3-4B-IT、Llama3.2-3B-Instruct）、3个任务（过度拒绝、工具过度使用、事实谄媚）的9个设置下，HeadEdit在7个设置上取得最优准确率，全部9个设置均优于基线模型；仅需50对样本即可超过基线效果，400对左右效果稳定，推理开销几乎可忽略，通用能力下降幅度远低于其他steering方法；已提取的子空间可直接复用于LoRA-DPO微调后的模型，在6个设置上进一步提升准确率。
### 核心结论
LLM的对齐失败很多时候不是模型没有学到正确行为的表征，而是未嵌入层的读出发阶段存在gap，仅通过输出端的轻量校正即可大幅提升效果，无需重新训练
