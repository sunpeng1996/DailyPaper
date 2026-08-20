---
title: 'Training Leaves Traces: Centered Residual Signatures for Language Model Lineage
  Verification'
title_zh: 训练留痕：基于中心化残差签名的大语言模型谱系验证方法
authors:
- Aman Singh Thakur
- Rayan Khoury
affiliations:
- Amazon, USA
- Massachusetts Institute of Technology, USA
arxiv_id: '2608.14929'
url: https://arxiv.org/abs/2608.14929
pdf_url: https://arxiv.org/pdf/2608.14929
published: '2026-08-13'
collected: '2026-08-20'
category: LLM
direction: 大语言模型 · 权重溯源与谱系验证
tags:
- LLM Lineage Verification
- Model Provenance
- Residual Signature
- White-box Verification
- Weight Trace
one_liner: 提出无数据白盒LLM谱系验证方法，可识别各类衍生同源权重，AUROC达1.0且速度超基线76倍
practical_value: '- 可复用该残差签名方法溯源业务中开源LLM的真实谱系，避免使用未授权衍生模型引发合规风险

  - 内部多团队共享微调LLM资产时，可基于该方法快速识别权重同源性，无需额外前向推理或标注数据

  - 针对LoRA合并、量化、剪枝后的模型版本溯源，可直接复用其中心化残差对齐的计算trick，效率远高于传统基线'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
开源大模型经过微调、LoRA合并、量化、剪枝、合并后常无来源记录，现有溯源方法要么易受权重修改影响、要么需要数据支撑或计算量极高，无法满足无数据快速溯源需求。
### 方法关键点
首先移除残差训练产生的通用身份对齐分量，跨残差块对比检查点特有的结构特征，生成对称谱系得分，用独立检查点做校准，全程无需任何数据输入。
### 关键结果数字
在残差MLP、GPT-2基准上，对微调、LoRA合并、剪枝、量化衍生模型与独立/蒸馏模型的区分AUROC达1.0；抗权重清洗实验中基线完全失效，该方法得分无变化，在GPT-2上速度比最优鲁棒基线快76×；在6个LLM架构上均有效，案例研究中100%正确识别3个同源、7个异源的公开LLaMA-2检查点。
