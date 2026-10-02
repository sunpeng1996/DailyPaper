---
title: 'E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models'
title_zh: 面向非因子化扩散语言模型的增强混合专家（E-MoE）模型
authors:
- Arseny Ivanov
- Alexander Kolesov
- Alexander Korotin
- Ivan Oseledets
- Mikhail Goncharov
affiliations:
- AXXX, Moscow
- Applied AI Institute, Moscow
arxiv_id: '2609.37533'
url: https://arxiv.org/abs/2609.37533
pdf_url: https://arxiv.org/pdf/2609.37533
published: '2026-09-28'
collected: '2026-10-02'
category: LLM
direction: 扩散语言模型 · MoE架构优化
tags:
- MoE
- Diffusion Language Model
- Masked Diffusion
- Discrete Latent
- Few-step Generation
one_liner: 复用MoE路由作为离散隐变量，无额外激活参数提升扩散LM少步生成质量
practical_value: '- 做电商商品文案、广告创意、搜索Query推荐等生成场景时，若采用扩散LM实现低延迟并行生成，可直接复用现有MoE结构的路由决策作为离散隐变量，无需新增VAE等额外模块，即可解决同步生成token语义不连贯问题，且不增加推理开销

  - 训练含MoE结构的模型时，可借鉴其对齐干净/噪声输入路由分布的KL损失设计，提升模型对带噪输入（如用户模糊Query、多模态噪声特征）的鲁棒性，无需额外标注数据

  - 对低延迟生成要求高的业务（如实时个性化push文案、直播口播脚本生成），E-MoE可在1-2步推理时实现2倍以上的生成质量提升，相同质量下可减少50%以上的推理步数，显著降低服务延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

#### 动机
掩码扩散语言模型（MDM）支持并行生成多token，推理延迟远低于自回归模型，但传统因子化反向过程忽略同步生成token间的相关性，少步生成质量差；现有连续隐变量优化方案需额外训练VAE，易发生后验坍缩且增加参数量，亟需无额外开销的因子化误差解决方案。
#### 方法关键点
- 复用MoE backbone原生路由决策作为离散共享隐变量，无新增参数与推理开销，同一路由器输入噪声序列、干净序列分别得到先验、后验分布，无需额外识别网络
- 推导离散隐变量下的ELBO上界作为训练目标，路由对齐损失简化为每层每token的分类KL散度，结合Gumbel-Softmax trick实现端到端训练
- 推理时仅需采样先验路由，每个NFE仅需1次前向传播，与因子化基线推理成本完全一致
#### 关键结果
在LM1B文本生成任务上对比MDLM、VADD等基线：NFE=1/2时生成困惑度比基线低2~2.6倍，MAUVE达基线的6~8倍，样本熵与基线持平无多样性损失；二值化MNIST任务上BPD低至0.062，优于VADD的0.064与MDLM的0.077，参数量与VADD基本持平。

MoE原生路由信号可作为免费离散隐变量，在不增加推理成本的前提下破解扩散LM的因子化误差瓶颈，大幅提升少步生成性能
