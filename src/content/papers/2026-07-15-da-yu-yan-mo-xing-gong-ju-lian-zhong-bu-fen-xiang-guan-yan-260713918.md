---
title: 'Partially Correlated Verifier Cascades in LLM Harnesses: Concave Log-Odds,
  Polynomial Reliability, and Blind-Spot Ceilings'
title_zh: 大语言模型工具链中部分相关验证器级联的可靠性理论
authors:
- Jiangang Han
affiliations:
- Independent Researcher
arxiv_id: '2607.13918'
url: https://arxiv.org/abs/2607.13918
pdf_url: https://arxiv.org/pdf/2607.13918
published: '2026-07-15'
collected: '2026-07-16'
category: LLM
direction: LLM可靠性 · 验证器级联理论
tags:
- LLM_Reliability
- Verifier_Cascade
- Correlated_Errors
- Blind_Spot
- Latent_Variable
one_liner: 提出可测量的部分相关验证级联理论，指出相关性让可靠性指数衰减退化为多项式级
practical_value: '- 做Agent/生成式推荐的内容正确性校验时，不要盲目堆叠同家族LLM验证器，相关性高时k=5就会把失败率低估20倍，优先换不同模型家族/模态/工具类验证器做去相关，比加验证次数性价比高得多

  - 可通过2次重复验证的结果快速计算验证器间相关性ρv，若ρv>0.3则停止增加同类型验证次数，转向引入外部结构化校验规则（如电商的价格合规、库存校验规则）

  - 设计生成式文案/商品推荐的核验链路时，需计算最优验证次数k†，避免验证过多反而误拒正确的个性化内容，导致推荐效果下降'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
原有Odds Law假设验证器条件独立，认为级联验证可让LLM输出错误率指数级下降，但实际同家族LLM生成器与验证器共享大量盲点，错误相关性极高，独立假设会严重高估系统可靠性，部分相关验证级联的严谨理论此前处于空白状态。

### 方法关键点
- 以潜变量α~G建模每个错误实例的验证器误接受率，G的上尾对应生成器-验证器的共享盲点区域
- 推导得到精确级联后验：ℓk = ℓ0 − ln m_k（m_k为G的k阶矩），证明ℓk对k呈凹性，独立假设的Odds Law是其在k=1处的切线与全局上界
- 引入单参数ρv（两次验证结果的类内相关系数）刻画验证器相关性，仅需2次重复验证即可测量；Beta分布假设下错误率随k呈多项式衰减1−r_k ≍ k^−b
- 存在α=1的盲点原子时，可靠性存在硬上限，无论增加多少级联验证都无法突破

### 关键结果
合成实验中，在¯α=0.3、ρv=0.3的真实场景下，独立假设在k=5时低估失败率20倍，k=10时低估≈3000倍；仅用R=8次验证结果拟合的相关理论可精准外推k=25的真实可靠性。

相关性不损害第一个验证器的效果，但会让后续验证的边际收益快速衰减，提升可靠性的核心是验证器去相关而非堆叠数量
