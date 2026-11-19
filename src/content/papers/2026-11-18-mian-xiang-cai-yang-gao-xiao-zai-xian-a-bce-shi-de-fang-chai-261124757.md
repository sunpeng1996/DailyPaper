---
title: Variance-Optimal Counterfactual Policy Design for Sample-Efficient Online A/B
  Testing
title_zh: 面向采样高效在线A/B测试的方差最优反事实策略设计
authors:
- Shashank Gupta
- Subhadeep Maji
affiliations:
- Microsoft, India
- DeepL, UK
arxiv_id: '2611.24757'
url: https://arxiv.org/abs/2611.24757
pdf_url: https://arxiv.org/pdf/2611.24757
published: '2026-11-18'
collected: '2026-11-19'
category: Eval
direction: 推荐系统A/B测试 · 方差优化
tags:
- A-B-testing
- off-policy-evaluation
- variance-reduction
- counterfactual-estimation
- contextual-bandits
one_liner: 联合优化动作级采样策略与控制变量，大幅降低A/B测试所需流量并提升统计功效
practical_value: '- 推荐/搜索新策略上线的A/B测试可直接复用本文动作级采样逻辑：优先采样新旧策略概率差大、奖励不确定性高的动作，流量最多可省61%，大幅缩短测试周期

  - 可复用成对反事实估计+控制变量的框架替代传统均值差估计，即使控制变量拟合不准也能保证ATE估计无偏，降低历史数据依赖

  - 工程落地可先上线Scalar版本，仅优化1个标量控制变量，开发成本极低即可拿到50%左右的流量节省收益，数据量充足再迭代Model-CV版本

  - 新增5%的均匀采样安全回退机制，避免极端采样导致的用户体验受损，同时满足IPS估计的full support条件'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统在线A/B测试的均值差估计方差高，当新旧推荐/搜索策略的动作（如商品、内容）重叠度高时，大部分流量采样的是概率差为0的无差异动作，仅引入噪声却无法提供有效信息，小效应量测试需要极长周期和海量流量；现有方差缩减方法要么仅优化事后估计器，要么仅优化全局流量分配，无法定向采样高信息价值的动作。
### 方法关键点
- 基于成对离策略评估Δ-IPS框架，无需将用户拆分为新旧策略两组，采用统一logging policy采样动作，通过加权计算得到无偏ATE估计
- 推导固定控制变量下方差最优动作级采样策略闭式解：动作采样概率与新旧策略的动作概率差绝对值、控制变量修正后的残差奖励二阶矩的平方根乘积成正比
- 联合优化采样策略与控制变量，提供两种落地方案：仅需优化1个参数的Scalar版本，和适配上下文/动作差异的Model-CV版本；新增5%均匀采样回退机制保证安全性
- 采用两阶段流程：先基于历史日志拟合奖励模型与控制变量，冻结设计后再采集测试数据，避免数据泄露
### 关键实验
在模拟contextual bandit环境（25维上下文、25/50/75个动作、小效应量ATE=0.005）测试，对比标准A/B、平衡A/B、重叠感知A/B等4个基线：
- Model-CV版本仅需平衡A/B 39%~51%的流量即可达到相同MSE，统计功效是平衡A/B的1.5~2.1倍，错选更差策略的概率降低42%~63%
- Scalar版本仅优化1个参数，也可将平衡A/B的流量需求降低47%~53%，效果接近Model-CV
### 核心结论
对于新旧策略重叠度高的小效应量A/B测试，优化动作级采样策略带来的流量效率提升远高于仅优化全局流量分配或事后估计器
