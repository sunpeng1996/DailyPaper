---
title: 'SP$^2$ec: Adaptive Self-Speculative Decoding for Vision-Language Models'
title_zh: SP²ec：面向视觉语言模型的自适应自投机解码算法
authors:
- Yuqi Huang
- Xingyao Li
- Yunlong Hou
- Fengzhuo Zhang
- Jiachun Pan
- Vincent Y. F. Tan
affiliations:
- National University of Singapore
- Yale University
arxiv_id: '2610.18735'
url: https://arxiv.org/abs/2610.18735
pdf_url: https://arxiv.org/pdf/2610.18735
published: '2026-10-13'
collected: '2026-10-14'
category: LLM
direction: 多模态大模型 · 推理加速优化
tags:
- Speculative Decoding
- VLM
- Bandit Algorithm
- Inference Optimization
- Self-Speculation
one_liner: 提出训练无关的单峰老虎机自适应自投机解码策略，为VLM推理带来最高11%的速度提升
practical_value: '- 电商多模态内容生成（商品文案、用户多模态咨询回复）场景可直接接入SP²ec作为推理加速组件，无需额外训练即可获得~10%的吞吐提升，无生成效果损失

  - 已接入SWIFT、SPECVLM等自投机解码方案的系统，可直接叠加SP²ec的单峰老虎机自适应配置选择策略，降低无效探索成本，避免固定配置在不同Query下的性能波动

  - 多模态Agent调用VLM时，可复用SP²ec的wall-time regret优化思路，根据当前Query动态选择最适配的模型剪枝/跳层配置，平衡推理精度与时延，适配实时交互场景

  - 生成式推荐场景下的纯文本LLM推理，只要自投机配置的吞吐符合单峰规律，即可直接复用该算法，无需重新开发自适应选择逻辑'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
投机解码是大模型推理加速的主流方案，但VLM的多模态输入、长上下文特性导致独立训练的小draft模型与目标模型对齐度波动大，加速效果不稳定。自投机解码复用目标模型部分层/Token作为draft，无需额外训练、对齐性更好，但最优draft配置（跳层数、保留视觉Token数等）随Query动态变化，固定配置无法适配所有场景；现有自适应方案多采用全量候选探索，探索成本过高，抵消加速收益。

### 方法关键点
- 验证自投机解码吞吐呈单峰分布：接受率随保留组件数增加边际收益递减，推理耗时随保留组件数线性增长，二者平衡出唯一最优吞吐点
- 提出SP²ec单峰老虎机算法，仅在当前最优配置的邻域（前后各1个候选）做探索，无需遍历全量配置，探索成本较全量探索方案降低80%以上
- 可作为插件直接叠加在SWIFT、KNAPSPEC、SPECVLM等主流自投机解码方案上，无需修改原方案逻辑，完全训练无关

### 关键实验
在Qwen2.5-VL-7B-Instruct、LLaVA-NeXT-Mistral-7B两个主流开源VLM，Video-MME、MMBench-Video等4个多模态数据集上验证：相比原自投机解码方案平均提速0.06~0.09x，最高提升0.12x；相比UCBSPEC自适应基线，非Top3配置的探索占比从49%~53%降至6%~16%，吞吐稳定更高。

自投机解码的吞吐天然符合单峰分布，仅在最优配置邻域做有限探索就能以极低开销实现近似最优的自适应加速，无需额外训练或数据标注。
