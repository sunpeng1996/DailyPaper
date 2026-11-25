---
title: Sample-Efficient In-Context Adaptation via Sleep
title_zh: 基于睡眠机制的样本高效上下文内适配方法
authors:
- Sangyun Lee
- Zhang Enyan
- Michael Xu
- Hao Tang
- Zinan Lin
- Weijia Xu
- Chris Quirk
- Jianfeng Gao
- Giulia Fanti
- Xiaodong Liu
affiliations:
- Carnegie Mellon University
- Yale University
- Microsoft Research
arxiv_id: '2611.32802'
url: https://arxiv.org/abs/2611.32802
pdf_url: https://arxiv.org/pdf/2611.32802
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: 大语言模型 · 上下文内适配效率优化
tags:
- In-Context Learning
- KV Cache
- Sample Efficiency
- Transformer
- Sleep Mechanism
one_liner: 为Transformer引入周期性睡眠阶段优化KV cache，大幅提升上下文内适配样本效率，几乎无额外推理开销
practical_value: '- 电商导购Agent场景下，可在用户输入间隙、等待工具返回的空闲时段触发睡眠流程，迭代优化历史对话KV cache，无需增加实时响应延迟即可提升用户偏好理解准确率

  - 生成式推荐场景可复用GRU风格的KV cache门控更新逻辑，在用户浏览过程中定时优化历史行为序列的KV表示，仅增加2%参数即可提升长序列推荐的样本效率

  - 长上下文用户行为建模的推荐场景，睡眠机制可在不增加KV缓存容量、不提升实时解码延迟的前提下，仅付出<8%的端到端延迟代价，获得2倍以上的上下文利用效率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型上下文内适配的样本效率远低于人类，靠扩模型规模提升效率的成本极高，推理端KV缓存、延迟开销随模型深度线性增长，无法支撑电商、Agent等场景下对长上下文用户信号的高效利用需求。

### 方法关键点
- 引入wake-sleep周期：每处理W个token的窗口后执行N-1次深度递归前向传播，迭代优化该窗口的KV cache，wake阶段正常解码无额外开销
- 训练时仅对wake阶段首趟前向传播的输出计算语言模型损失，sleep阶段的优化效果通过更新后的KV缓存作用于后续窗口预测，全程不截断梯度
- 新增GRU风格的门控机制控制KV缓存更新，仅增加<2%参数量，避免sleep阶段更新覆盖原有低阶特征
- sleep阶段使用双向注意力，无需遵循因果掩码，提升上下文表示优化效率

### 关键结果
在1.2B参数Transformer上验证，对比无睡眠baseline：
1. N=2、N=4睡眠模型达到相同next token损失时，分别少用2.10×、2.39×的上下文token
2. 端到端解码延迟仅增加2.6%（N=2）、7.6%（N=4），KV缓存开销几乎无增长
3. 各类少样本学习任务上，睡眠模型准确率随样本量增长的提升幅度显著高于baseline，无睡眠模型易出现性能瓶颈

最值得记住的一句话：当模型有足够上下文和时间适配时，学习曲线的斜率比模型已有的知识更重要
