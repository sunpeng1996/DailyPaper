---
title: Is SwiGLU's Open Positive Tail Necessary? Evidence from Closed-Tail Gating
  with MemGLU
title_zh: 闭尾门控MemGLU验证：SwiGLU开放正尾并非小模型预训练必需
authors:
- Yuting Ge
- Pengju Yang
- Mingkai Nie
affiliations:
- City University of Hong Kong
- Beihang University
- National University of Singapore
arxiv_id: '2608.07323'
url: https://arxiv.org/abs/2608.07323
pdf_url: https://arxiv.org/pdf/2608.07323
published: '2026-08-07'
collected: '2026-08-10'
category: LLM
direction: 大模型基础组件 · 激活函数优化
tags:
- SwiGLU
- MemGLU
- Activation Function
- FFN
- Decoder-only LLM
one_liner: 提出闭尾激活MemGLU，9M/30M LLM上与SwiGLU性能差小于0.1%，验证开放正尾非必需
practical_value: '- 电商/推荐域小参数量垂直LLM（如文案生成、意图理解模型）可尝试替换SwiGLU为MemGLU，性能损失<0.1%可忽略，闭尾特性还能降低数值溢出风险

  - 业务小模型激活函数选型无需默认绑定SwiGLU，可基于自身场景做闭尾/开尾激活的AB测试，选择性价比更高的方案

  - 预训练阶段需锁定激活函数形态，已训完的SwiGLU模型不要擅自修改正尾逻辑，会导致性能显著下降

  - 端侧部署的小LLM可优先测试MemGLU这类闭尾激活，数值范围可控性更高，有助于降低量化损失，压缩部署成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
SwiGLU是LLaMA、Qwen等主流Decoder-only LLM的FFN默认门控激活，其正域线性增长的开放尾被默认认为是性能必需，但一直缺乏严格对照实验验证该设计的必要性，小参数量场景下是否存在更适配的闭尾激活方案待探索。

### 方法关键点
- 提出MemGLU闭尾激活，函数形式为$c_0 \times tanh(g) \times sech(g)$，正负域输出均收敛到0，无开放正尾；仅替换SwiGLU的标量门控，FFN参数规模、投影结构完全不变
- 采用配对训练控制变量：同初始化权重、同数据顺序、同训练配置，仅激活函数不同，排除其他变量干扰
- 做RMS校准，调整系数$c_0$让MemGLU初始化时的输出RMS与SwiGLU对齐，保证训练初始状态一致

### 关键实验
在9M、30M两个参数量的Decoder-only LLM上做预训练，对比基线为原生SwiGLU：9M尺度下RMS校准的MemGLU验证NLL比SwiGLU低0.111%，30M尺度下高0.122%，双向差距均小于0.1%；对训好的SwiGLU做正尾抑制，9M/30M模型NLL最高分别上涨0.403、0.960，对正尾改动高度敏感。

### 核心结论
小参数量Decoder-only LLM训练中，SwiGLU的开放正尾并非性能必需，模型会自适应预训练阶段的门控几何形态。
