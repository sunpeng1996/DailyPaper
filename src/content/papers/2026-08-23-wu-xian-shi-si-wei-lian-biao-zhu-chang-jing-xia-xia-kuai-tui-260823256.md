---
title: Is Next-Chunk Reasoning RL Really Better than SFT? Revisiting Training Strategies
  under no-CoT Data
title_zh: 无显式思维链标注场景下下块推理RL真的优于SFT吗
authors:
- Yinhao Tang
- Youqing Fang
- Yanan Sun
- Jiangning Liu
- Ziyi Wang
- Xun Zhao
- Weiming Zhang
- Bin Liu
- Kuikun Liu
- Wenwei Zhang
affiliations:
- University of Science and Technology of China
- Shanghai AI Laboratory
arxiv_id: '2608.23256'
url: https://arxiv.org/abs/2608.23256
pdf_url: https://arxiv.org/pdf/2608.23256
published: '2026-08-23'
collected: '2026-08-27'
category: Training
direction: 大模型推理训练 · 无标注数据利用
tags:
- Chain-of-Thought
- SFT
- Reinforcement Learning
- No-CoT Data
- Training Efficiency
one_liner: 提出混合SFT基线，证实无CoT数据场景下其效果优于下块推理RL且算力低60倍以上
practical_value: '- 做LLM增强的商品理解、用户意图建模时，若有大量无标注业务数据（商品详情、用户评价、行为日志），优先采用Mixed SFT同时喂标注指令数据和无标注业务数据，比分阶段SFT减少知识遗忘，成本远低于RL方案

  - 搭建电商Agent、导购Agent的推理链路时，不要盲目加RL阶段提效果，先把SFT的数据配比、混合方式优化到位，大部分场景下SFT优化的ROI更高

  - 评估微调中间版本时不要只看即时对话/推理准确率，要结合下游对齐、业务上线的最终效果，中间指标低不代表最终落地效果差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前推理大模型训练高度依赖标注成本极高的长CoT数据，而大量无显式推理标注的no-CoT数据（比如习题解答、教材推导、业务非结构化文本）尚未被高效利用。此前提出的下块推理RL（NCR）方案宣称比SFT更适合利用这类数据，但对比基线仅为仅用no-CoT数据训的SFT，未考虑合理的SFT方案，收益来源不明确。
### 方法关键点
- 提出此前被忽略的Mixed SFT基线：单阶段同时在长CoT标注数据和no-CoT无标注数据上做SFT，对比三类基线：下块推理RL（细粒度NTR、粗粒度NSR）、分阶段SFT（先训no-CoT再训长CoT的Sequential SFT）、仅用长CoT的Reasoning SFT
- 所有策略统一后续接相同的RLVR（带可验证奖励的RL）阶段，以最终post-RLVR准确率作为核心评估指标，避免中间指标偏差。
### 关键实验结果
基于AoPS爬取的152K条长CoT标注数据、421K条no-CoT解答数据，后续RLVR用DAPO-Math-17K数据集，在6个数学推理域内、3个跨域benchmark上测试：
- Mixed SFT的post-RLVR平均准确率比NTR高3.1个百分点、比NSR高3.7个百分点，训练GPU耗时仅为NCR类方法的1/60
- Mixed SFT的pre-RLVR准确率比其他方法低近20个百分点，但最终post-RLVR准确率最高，跨域泛化性也最优。
### 最值得记住的结论
在利用no-CoT数据做推理模型训练时，优化SFT阶段的数据混合方式的性价比远高于引入额外的RL推理重建阶段，pre-RLVR的中间指标无法预测最终对齐后的效果。
