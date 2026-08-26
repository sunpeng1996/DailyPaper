---
title: 'The Mask Is Not the Model: Auditing Prefix Invariance in Attention, State-Space,
  and Hybrid Sequence Models'
title_zh: 混合序列模型前缀不变性审计：轻量化因果泄漏检测与层级定位
authors:
- Taebong Kim
- Youngsik Hong
- Minsik Kim
- Sunyoung Choi
- Jaewon Jang
- Minseo Kim
affiliations:
- VIDRAFT AI Research
- QuantumOS, Seoul, Republic of Korea
arxiv_id: '2608.22876'
url: https://arxiv.org/abs/2608.22876
pdf_url: https://arxiv.org/pdf/2608.22876
published: '2026-08-23'
collected: '2026-08-26'
category: LLM
direction: 大模型 · 因果正确性审计
tags:
- Causal Leakage
- Prefix Invariance
- Model Auditing
- Hybrid Sequence Model
- LLM Validation
one_liner: 提出仅需两次前向传播的无梯度检测方法，精准定位因果泄漏的具体层
practical_value: '- 自研/微调用于生成式推荐文案、Agent推理的混合架构LLM时，可复用该2次前向传播的检测方法替代仅检查attention
  mask的流程，避免因果泄漏导致的KV cache复用失效、生成结果异常问题

  - LoRA微调电商/广告领域小模型时，若自定义了层结构/注意力逻辑，可将该审计加入单测环节，避免实现bug导致训练指标虚高、部署后生成效果退化

  - 接入第三方开源混合架构LLM时，可先用该方法做正确性校验，测试序列长度需超过模型声明的chunk、滑动窗口、卷积核大小，避免踩中开源实现隐式bug'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前混合序列模型（注意力+SSM/卷积/递归等架构）广泛应用，原有的仅检查attention mask的因果正确性验证方法完全失效；因果泄漏不会触发显式报错，反而会让训练loss、验证PPL等指标虚高，直到部署后自由生成、KV cache复用、speculative decoding时才会暴露问题，排查成本极高，此前缺乏统一的轻量化检测方案。
### 方法关键点
- 形式化定义前缀不变性：若两个序列前t个token完全一致，所有层的第t位表征必须完全一致，与t之后的token无关
- 检测流程仅需2次无梯度前向传播：构造仅最后1个token不同的两个等长序列，通过hook获取每层输出，对比前T-1位的表征差，首个差值超过阈值的层即为泄漏层
- 关键设计：关闭KV cache确保两次前向路径一致，仅对比前缀排除扰动位置的合法差异，单页可复现，CPU运行仅需0.1~0.5s
### 关键结果
- 在8种不同架构（Transformer、RWKV、Mamba、混合架构）的checkpoint上完成192次故障注入，该方法100%精准定位到注入层，传统mask检查检测率为0，logits-only扰动检查无法定位层
- 静态分析transformers库的chunked-scan实现，发现Zamba2、Nemotron-H两个开源模型存在因果泄漏，2行代码修复后泄漏完全消失
### 核心结论
因果正确性是所有自回归模型应用的前提，仅检查attention mask无法验证因果性，前缀不变性审计必须成为模型上线前的强制检查项，且测试序列长度必须超过模型的chunk、窗口、卷积核参数。
