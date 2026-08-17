---
title: 'You Only Pass Once: Answering and Abstaining Together in a Single Forward
  Pass of a Frozen Language Model'
title_zh: YOPO：冻结大模型单次前向同时实现推理回答与置信度拒答
authors:
- Ziyang Luo
- Zhongyao Chu
- Xinjie He
- Youting Wang
- Xukui Qin
- Runxiong Wu
- Yan-Syuan Chen
affiliations:
- Georgia Tech
- Columbia University
- University of Wisconsin-Madison
- University of Texas at Austin
arxiv_id: '2608.14465'
url: https://arxiv.org/abs/2608.14465
pdf_url: https://arxiv.org/pdf/2608.14465
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: LLM推理优化 · 残差流干预
tags:
- Frozen-LLM
- Activation-Steering
- Residual-Stream
- Confidence-Abstention
- Inference-Optimization
one_liner: 通过残差流无标签校正实现冻结LLM单次前向同时完成增强推理与信息不足拒答，推理成本减半
practical_value: '- 电商商品问答、智能客服场景可复用残差流零样本sufficiency方向实现无标注拒答，跨域稳定性比标注训练的拒答高30%以上，有效规避幻觉

  - 小参数冻结LLM部署时，可采用本文残差校正方案，仅加约1%参数量的探针、不增加推理次数，同时获得推理效果提升和拒答能力，推理成本比双次前向降50%

  - 跨域部署拒答能力时，优先在最难源域（如多跳问答数据）拟合sufficiency方向，跨域迁移效果比普通源域高10pp以上，无需目标域标注

  - 生成式推荐的幻觉防控可直接复用残差读出头方案，在生成侧加轻量门控，无需改动推荐大模型本身，即可自动拦截低置信推荐项'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
冻结LLM在推理任务中存在两个核心痛点：一是残差流已编码的证据未被充分利用，推理准确率偏低；二是无法感知输入信息不足，易产生幻觉。现有方案需两次前向分别实现推理增强和置信度判断，推理成本翻倍，小参数模型部署性价比极低。
### 方法关键点
- 推理增强：在冻结LLM中间层部署轻量条件转向探针（仅占backbone 1%参数量），输入依赖地修改残差流提升推理效果，主干完全冻结可快速插拔
- 零样本拒答：预计算sufficiency方向`d`，通过残差投影判断输入信息是否充足，无需拒答标注训练，跨域稳定性高
- 无标签校正：训练小网络`M`，仅用<转向后残差、原始残差>对做MSE损失拟合，消除转向操作对拒答信号的干扰，全程不接触拒答标注，保留`d`的跨域能力
- 可选旗舰配置：叠加小参数量BCE监督头提升域内效果，明确量化其域内效果-跨域迁移的trade-off
### 关键结果
- 覆盖αNLI、SQuAD2、RepLiQA、MuSiQue等6类数据集，跨10个不同架构、0.5B~7B规模的冻结LLM验证
- 1.5B Qwen2.5上，端到端3分类准确率（答对/拒答/答错）从冻结基线0.375提升至0.798，比双次前向参考方案高4.5pp；跨域AUROC从0.836提升至0.888，仅比双次前向低3pp
- 10个测试backbone上，单次前向方案的端到端效果全部超过双次前向参考，域内拒答AUROC最高达0.997

> 最值得记住的结论：拒答能力应该从残差流读取而非训练进模型权重，前者跨域稳定性比后者高20pp以上，小模型部署优先用无标签校正方案平衡效果、成本与迁移性
