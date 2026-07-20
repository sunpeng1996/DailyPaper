---
title: 'Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D'
title_zh: 前沿大模型难以精准复制文本：采用二维视角建模提升基础能力
authors:
- Haodong Wen
- Yiran Zhang
- Yingfa Chen
- Kaifeng Lyu
affiliations:
- Tsinghua University
arxiv_id: '2607.16072'
url: https://arxiv.org/abs/2607.16072
pdf_url: https://arxiv.org/pdf/2607.16072
published: '2026-07-17'
collected: '2026-07-20'
category: LLM
direction: 大语言模型 · 二维位置编码优化
tags:
- RoPE
- positional encoding
- length generalization
- copy task
- 2D-RoPE
one_liner: 发现前沿LLM复制任务失效，提出2D-RoPE位置编码，大幅提升复制任务长度泛化能力
practical_value: '- 做Agent工具调用、结构化参数提取场景时，可将输入输出用换行分隔，触发2D-RoPE的同列对齐能力，大幅减少内容复制错误

  - 生成式推荐/广告文案生成中，若需从用户输入的结构化信息（规格、参数列表）精准提取字段，可参考2D-RoPE设计给结构化文本分配二维位置ID，降低重复内容匹配错误

  - 业务中微调小模型做精准内容提取/格式转换任务（如用户列表转JSON/CSV），可引入2D-RoPE替代标准RoPE，小样本即可实现远超基线的长度泛化，无需大量长序列训练数据'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前前沿LLM可秒解复杂推理任务，但在上下文窗口内的精准文本复制任务上表现极差，输入含大量重复子串、长度较长时准确率常低于50%；复制是Agent工具调用、结构化信息处理的基础能力，现有1D位置编码（如RoPE）的归纳偏置依赖局部上下文匹配，无法很好处理长度相关的位置偏移，导致复制失效。
### 方法关键点
- 提出2D-RoPE位置编码，以换行符为行分隔符，给每个token分配（行ID, 列ID）二维位置，将头维度拆分为两部分分别编码行、列相对位置，把复制任务转化为固定列偏移的token检索，大幅降低学习难度。
- 提出Auto-2D-RoPE变体，无需显式换行符，通过学习的线性投影自动预测每个token的二维坐标，适配无显式格式标记的文本场景。
- 可搭配Hybrid-RoPE方案，交替使用RoPE和2D-RoPE，平衡通用语言建模和复制能力。
### 关键实验
- 对比基线覆盖GPT-5.5、Claude Opus 4.7、Gemini 3.1 Pro等前沿闭源模型，以及Qwen3系列开源模型的标准RoPE版本。
- 合成实验中，1层2D-RoPE仅训练长度1-100的样本，可实现最长1000×长度泛化，复制准确率100%；12层模型实现100×长度泛化。
- 1.4B参数2D-RoPE预训练后微调，8K长度递归翻转二进制复制任务准确率达87.3%，标准RoPE基线准确率为0；Python列表转换任务训练长度仅50-150，可泛化到3倍以上长度，准确率接近100%。
- 2D-RoPE在常识推理任务上表现与标准RoPE相当，无通用能力损失。
### 核心结论
文本本身隐含二维结构（换行、段落、列表等），利用这类结构设计位置编码，能以极低代价大幅提升LLM基础操作能力，且不损失通用性能。
