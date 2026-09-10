---
title: When Does Low-Bit Quantization Preserve the Decisions of Vector Search?
title_zh: 低比特量化保留向量搜索决策的边界条件与稳定性理论
authors:
- Wenxuan Xiao
- Xu Cao
affiliations:
- Astrmira Tech
arxiv_id: '2609.09854'
url: https://arxiv.org/abs/2609.09854
pdf_url: https://arxiv.org/pdf/2609.09854
published: '2026-09-09'
collected: '2026-09-10'
category: RecSys
direction: 向量检索 · 低比特量化优化
tags:
- Vector Search
- Low-bit Quantization
- Decision Stability
- Graph-based ANN
- Recall Optimization
one_liner: 从决策粒度而非全局保真度建立低比特向量搜索的稳定性理论与验证框架
practical_value: '- 向量召回量化选型不要只看全局Spearman相关/MSE，要在业务真实的top-K候选集上测排序/剪枝翻转率，全局保真度和实际召回效果可能完全脱钩，比如论文中Cohere嵌入旋转后全局相关提升0.35，但锚定top1的排序翻转率反而升高50%

  - 可落地标准化margin诊断指标M=c_QΓ/v，提前筛出风险决策：M>5的决策几乎不会出现量化翻转，M<1的翻转率超过25%，可针对低margin请求走精确打分兜底，在可控算力损耗下降低量化带来的召回损失

  - 低比特量化适配前先做准入校验：如果嵌入的量化校准斜率接近0、残差尾重超过高斯分布2倍以上，直接放弃坐标二进制量化，改用随机旋转+RaBitQ等方案修复，避免出现类似GIST数据集上召回退化到2%的极端问题'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有低比特向量量化的评估依赖全局距离保真度（MSE、Spearman相关），但图向量搜索的核心执行逻辑是大量二值比较决策（排序、剪枝），全局指标完全无法反映真实决策错误：同样2比特坐标量化在Cohere文本嵌入上召回@10达95%，在GIST图像描述符上仅2%，传统分析无法解释该差异。
### 方法关键点
- 无分布假设的决策风险分解：排序/剪枝翻转概率拆分为边界质量（精确margin接近0的概率）+残差尾概率，独立拆解两个误差来源
- 纳入共享query/节点的残差相关性：修正传统独立假设下的残差方差高估问题，Cohere嵌入场景下忽略相关性会把残差方差高估7.4倍
- Vamana图索引冻结轨迹耦合定理：量化输出与精确结果一致当且仅当每一步局部决策一致，可从局部风险上推全局召回风险
- 无模型依赖的留出块证书方法，仅用离线数据即可给量化决策错误率提供统计保证
### 关键实验
在Cohere、MiniLM、GIST等12个公开嵌入数据集验证，标准化margin预测排序/剪枝翻转率的Spearman相关分别达0.97/0.99，远高于全局保真度的0.74/0.05；960次Vamana索引构建调用完全符合耦合定理；随机旋转将Cohere全局保真度从0.58提升到0.93，但锚定top1的排序翻转率反而从5.83%升至8.81%。
### 核心结论
低比特向量搜索的效果不能用单一保真度数字衡量，错误决策集中在小margin区域，全局指标会抹去共享结构带来的噪声相关性
