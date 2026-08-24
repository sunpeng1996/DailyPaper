---
title: Rethinking Expressivity and Efficiency in Test-Time Training
title_zh: 兼顾表达性与效率的测试时训练（TTT）优化方法E2-TTT
authors:
- Zeyun Zhong
- Joya Chen
- Manuel Martin
- Frederik Diederichs
- Juergen Gall
- Juergen Beyerer
affiliations:
- Karlsruhe Institute of Technology
- National University of Singapore
- Fraunhofer IOSB
- Lamarr Institute for Machine Learning and Artificial Intelligence
- University of Bonn
arxiv_id: '2608.21308'
url: https://arxiv.org/abs/2608.21308
pdf_url: https://arxiv.org/pdf/2608.21308
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 长上下文LLM · 测试时训练优化
tags:
- Test-Time Training
- Long Context
- Length Extrapolation
- Chunk Processing
- In-context Retrieval
one_liner: 推导闭式并行标量核，实现token级表达性与chunk级训练效率兼得的TTT架构
practical_value: '- 长上下文Agent/商品检索业务可借鉴E2-TTT的chunk级并行+token级动态保留设计，替代现有KV cache方案，在不损失检索精度的前提下提升长序列处理吞吐

  - 跨域/增量用户兴趣建模场景可复用测试时训练的轻量fast weight更新思路，无需全量微调即可在线适配用户实时行为，降低推理端更新成本

  - 长视频/多模态商品内容理解场景可采用「冻结大模型主干+仅训练TTT参数」的适配方案，用极少参数量达到全量微调效果，降低定制化训练成本

  - 有长度外推需求的场景（如用户长行为序列召回），可参考E2-TTT搭配滑动窗口注意力的混合架构，在训练上下文外也能保持稳定的召回精度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Test-Time Training（TTT）方法存在难以调和的 trade-off：token级更新表达性强但受限于串行依赖，训练速度慢、硬件利用率低；chunk级更新效率高但通过平均简化更新规则，丢失了chunk内token的时间权重信息，长上下文外推和检索性能大幅下降，无法同时满足工业界对效果和吞吐的要求。

### 方法关键点
- 推导闭式并行标量核，在chunk起始权重取梯度的标准近似下，直接计算得到chunk结束时的fast weight和动量状态，完全复现token级更新的动态效果，同时支持全并行chunk级训练
- 采用混合架构：E2-TTT模块建模长程依赖，搭配滑动窗口注意力捕捉局部依赖，两路输出通过输入依赖的动态门控融合
- 支持输入依赖的token级学习率、动量、衰减系数调节，fast weight网络支持GELU MLP、SwiGLU MLP两种配置，仅用语言模型损失端到端训练，无额外辅助目标

### 关键结果数字
- 1.3B参数版本在LAMBADA数据集perplexity低至15.3，优于现有最强baseline的16.1，语言建模效果与主流TTT、混合注意力方案相当
- 长度外推性能突出：在「Needle in a Haystack」passkey测试中，训练上下文为2K，8倍外推到16K时仍保持90%以上准确率，远高于baseline在4K就崩溃的表现
- LongBench长上下文理解基准上，1.3B SwiGLU版本平均准确率14.1%，优于Mamba2（10.3%）、HQLT（12.1%）、LaCT（7.7%）
- 多模态适配：集成到Qwen3VL-2B-Instruct时，仅训练TTT参数即可达到全量微调的效果，VideoMMMU准确率43.9%，LongVideoBench得分59.0

### 核心结论
保留精确的token级时间动态是长上下文泛化的核心，通过闭式核推导可以在不损失训练效率的前提下实现这一点
