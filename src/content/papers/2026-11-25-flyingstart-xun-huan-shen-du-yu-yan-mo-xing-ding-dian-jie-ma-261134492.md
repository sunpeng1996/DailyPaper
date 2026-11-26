---
title: 'FlyingStart: Learned Cross-Token Warm Starts for Fixed-Point Decoding in Recurrent-Depth
  Language Models'
title_zh: FlyingStart：循环深度语言模型定点解码的跨Token学习暖启动
authors:
- Runguo Li
- Dezhen Lu
- Zixiang Ni
affiliations:
- University of Illinois Urbana-Champaign
- University of Tübingen
- Xi'an Jiaotong University
arxiv_id: '2611.34492'
url: https://arxiv.org/abs/2611.34492
pdf_url: https://arxiv.org/pdf/2611.34492
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: 循环深度LLM · 推理加速 · 暖启动优化
tags:
- Recurrent-Depth LM
- Warm Start
- Fixed-Point Decoding
- Inference Acceleration
- KV Cache
one_liner: 为循环深度语言模型提供无精度损失的低成本跨Token解码暖启动，降低14-19%解码层消耗
practical_value: '- 若业务中用循环深度LLM做Agent多轮推理、生成式推荐文案/商品标题，可直接集成FlyingStart方案：仅需几百条业务领域文本做岭回归校准，几分钟即可完成适配，无需修改模型权重，在不降精度的前提下提升16-18%解码吞吐，降低推理成本

  - 暖启动思路可迁移到其他迭代式业务场景：比如RAG的多轮召回迭代、多阶段精排模型的迭代打分，用上一步的输出做线性映射作为当前步的初始化值，可有效减少迭代次数，降本提效

  - 该方案和现有LLM推理优化技术完全兼容，可与自投机解码、KV cache压缩、动态批处理等方案叠加使用，比如叠在WaveFront自投机解码上还能额外提升10-14%的吞吐'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
循环深度（Looped）LLM通过复用同一块层迭代生成Token，参数效率高但推理成本高；现有优化都只关注何时停止迭代，所有Token都从随机噪声初始化，浪费了前序Token的收敛状态信息，直接复用前序Token状态又和当前Token定点距离过远，没有收益。

### 方法关键点
- 核心发现：相邻Token的定点状态存在线性关联，通过岭回归拟合线性映射W，将前序Token的退出状态、当前Token的前置层输出拼接后映射为当前Token的迭代初始值，成本不到单轮迭代的5%
- 完全兼容原有逻辑：不修改模型权重、迭代规则和退出条件，原有退出准则依然能保证精度，预测不准只会增加迭代次数不会降精度，无需投机解码的验证步骤
- 校准成本极低：仅需几百条文本序列（约20k Token即可达到最优效果），在冻结模型上跑一次全深度前向即可闭集求解W，无需梯度训练，几分钟就能完成

### 关键结果
在Huginn-0.125 3.5B模型上测试，同等精度下比最强无训练基线少14-19%解码层，在2个不同的服务引擎上批量吞吐提升16-18%，叠加WaveFront自投机解码还能再提10-14%；在4个数学推理数据集、维基百科、代码生成、BBH等任务上均验证有效，小样本校准数据就能适配领域场景。

### 核心结论
循环深度LLM的推理优化除了控制迭代停止时机，迭代初始值是另一个可独立调节的低成本杠杆，收敛越慢的模型收益越高。
