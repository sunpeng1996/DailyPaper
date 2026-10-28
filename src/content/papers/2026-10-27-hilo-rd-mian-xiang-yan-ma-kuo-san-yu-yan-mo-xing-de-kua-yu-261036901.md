---
title: 'HiLo-RD: Cross-Budget Self-Distillation for Masked Diffusion Language Models'
title_zh: HiLo-RD：面向掩码扩散语言模型的跨预算自蒸馏方法
authors:
- Xiang Li
- Chengting Yu
- Jungang Li
- Yilun Zheng
- Junzhuo Li
- Xingyao Zhang
- Wenbo Su
- Xuming Hu
affiliations:
- 香港科技大学（广州）
- 浙江大学
- 南洋理工大学
- 阿里巴巴集团
- 香港科技大学
arxiv_id: '2610.36901'
url: https://arxiv.org/abs/2610.36901
pdf_url: https://arxiv.org/pdf/2610.36901
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: 扩散大模型 · 跨预算自蒸馏优化
tags:
- Diffusion LLM
- Self-Distillation
- LoRA
- Low Budget Inference
- Knowledge Distillation
one_liner: 将同模型大窗口高预算推理能力蒸馏到小窗口低预算解码，缓解过早承诺问题
practical_value: '- 电商智能客服、商品文案生成等场景可复用跨预算蒸馏思路：用同模型高预算下的优质生成轨迹蒸馏到低预算部署模型，不增加推理成本即可提升生成质量、缩短响应长度

  - 扩散模型部署优化可直接复用clean EOT提前停止规则：在不损失生成效果的前提下减少无效解码步数，降低推理时延

  - 蒸馏实现无需外部教师，仅对齐同模型不同预算下的隐藏表示配合LoRA轻量化微调，适配业务小样本快速迭代需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
掩码扩散语言模型（MDLM）支持双向注意力、非顺序生成，推理能力优于自回归模型，但受限于推理预算（窗口大小、迭代步数）会出现预算诱导的过早承诺问题：小窗口下模型会提前固定尾部回答片段作为后续推理的上下文，导致最终结果错误。相同模型在大窗口高预算下推理准确率更高、响应更短，但大窗口部署成本过高，现有方法无法直接将大窗口的优质推理能力迁移到小窗口低预算场景。
### 方法关键点
- 以同模型大窗口高预算推理轨迹为冻结教师，小窗口低预算模型为学生，采用LoRA做轻量化微调，无需额外标注数据
- 训练时将大窗口推理状态裁剪为小窗口视图，对齐二者在已提交token位置的隐藏表示MSE损失，同时优化token预测和提交顺序
- 设计clean EOT提前停止规则：检测到最左侧已提交EOT且前序所有位置都已提交时终止解码，减少无效计算
### 关键实验结果
在GSM8K、MATH500数学推理基准及HumanEval、MBPP代码生成基准上对比LLaDA-8B、Masked SFT、Diffu-GRPO等基线：GSM8K准确率从68.84%提升至78.24%（+9.4pp），平均可读长度从362.8降到271.3（缩短约25%）；MBPP Pass@1从38.6%提升至41.4%，推理时间从19.51s降到11.2s，均无需额外领域训练。
最值得记住的结论：Think Wide, Reason Lean，用高预算宽推理得到的优质轨迹蒸馏到低预算部署模型，可同时提升效果、降低推理成本。
