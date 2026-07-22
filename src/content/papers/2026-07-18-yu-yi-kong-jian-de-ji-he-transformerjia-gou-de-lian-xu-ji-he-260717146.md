---
title: 'The Geometry of Semantic Space: A Continuous Geometric Framework for the Transformer
  Architecture'
title_zh: 语义空间的几何：Transformer架构的连续几何框架
authors:
- Zhihua Liang
affiliations:
- INFN, Sezione di Cagliari, Italy
arxiv_id: '2607.17146'
url: https://arxiv.org/abs/2607.17146
pdf_url: https://arxiv.org/pdf/2607.17146
published: '2026-07-18'
collected: '2026-07-22'
category: LLM
direction: 大模型基础理论 · Transformer几何建模
tags:
- Transformer
- LLM
- Differential Geometry
- Semantic Space
- Attention Mechanism
one_liner: 将Transformer核心组件映射为微分几何流方程，可预测LLM稳定性、上下文边界与优化动态
practical_value: '- 可复用文中Attention Sink的对数缩放规律，优化长上下文LLM的滑动窗口截断策略，平衡长程用户行为召回能力和计算成本

  - 文中推导的RMSNorm的$ϵ$参数与Lipschitz常数的$ϵ^{-1/2}$定量关系，可用于调整LLM微调时的数值稳定性参数，降低LoRA微调的梯度爆炸概率

  - 基于RoPE的拓扑稳定性结论，可指导长序列推荐场景下的用户行为序列位置编码设计，缓解长序列表征漂移问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Transformer理论分析多基于离散代数视角，难以统一解释RoPE长程衰减、Attention Sink、上下文长度边界、训练稳定性等分散的经验现象，缺乏可量化预测的统一理论框架。
### 方法关键点
- 基于单条几何公理：token序列是配备正则测度格的离散1维流形，将Transformer所有核心组件（RMSNorm、RoPE、Softmax Attention、FFN、残差流、SGD、权重衰减）全部映射为微分几何、测度论、随机微积分术语
- 构建语义纤维丛$E=M \times R^d$模型，将Attention建模为熵最优输运的薛定谔桥，SGD建模为违反细致平衡的伊藤扩散过程
- 推导得出拓扑稳定性对偶定律、RoPE环面庞加莱重现的$O(1/\sqrt{k})$热力学抑制、上下文长度相变等可验证的定量预测
### 关键实验
在Qwen3、LLaMA-3.1、Gemma-3、GPT-2、Mistral共5种架构，参数量124M~8B范围开展6组实验，验证结果与理论预测完全匹配：$ϵ^{-1/2}$利普希茨缩放校准的$R^2=1.000$，覆盖AdamW和纯SGD两种优化器排除动量干扰，所有拓扑、热力学预测均达到机器精度级吻合。
### 核心结论
Transformer的所有核心经验现象本质上都是其对应连续几何框架的拓扑约束的显性表现，可通过几何定量计算提前预测而非仅靠实验试错。
