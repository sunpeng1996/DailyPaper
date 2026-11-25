---
title: 'Latent Merger: Latent-Space Composition of Hypernetwork-Generated LoRAs'
title_zh: Latent Merger：超网络生成LoRA的隐空间融合方法
authors:
- Yanlai Yang
- Minki Kang
- Divyam Madaan
- Sung Ju Hwang
- Mengye Ren
affiliations:
- New York University
- KAIST
- DeepAuto.ai
arxiv_id: '2611.33048'
url: https://arxiv.org/abs/2611.33048
pdf_url: https://arxiv.org/pdf/2611.33048
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM参数高效微调 · LoRA融合
tags:
- LoRA
- Hypernetwork
- ModelMerging
- KnowledgeInjection
- LatentSpace
one_liner: 在隐空间融合超网络生成的多文档LoRA，固定秩下性能优于权重/因子空间融合方法
practical_value: '- 业务中使用超网络生成多场景/多类目LoRA时，不要用传统TIES/DARE/SVD等权重空间合并方法，优先在超网络中间隐空间做融合，可大幅提升合并后性能，同时推理延迟降低1-2个数量级

  - 训练轻量LoRA融合模块时，优先选择KL散度蒸馏目标对齐单场景Oracle LoRA的输出分布，比直接用交叉熵监督效果更好；全程冻结基座LLM和超网络，仅训练3层小Transformer融合模块，单A100即可完成训练，适配业务快速迭代需求

  - 面向电商客服/导购Agent的多文档知识注入场景，可通过该方法将多份商品规则、活动政策、商家须知等文档对应的LoRA合并为单个固定秩LoRA，无需在prompt中拼接长上下文，也无需维护大量LoRA适配器，显著降低存储和推理成本'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
超网络可通过单次前向传播将文档转换为LoRA适配器，实现LLM的快速知识注入，但流式场景下每份文档存储独立LoRA存储成本过高，多文档查询时加载多个LoRA会显著提升推理成本。传统权重/因子空间LoRA合并方法针对梯度微调的LoRA设计，而超网络生成的LoRA几何结构差异较大，直接合并性能衰减明显。
### 方法关键点
- 先验证超网络生成的LoRA相比梯度微调LoRA，谱集中度更高、跨文档余弦相似度更大，在适配器空间分布更紧凑，适配隐空间融合
- 框架由三部分组成：冻结超网络编码器将每份文档映射为隐向量；轻量可训Latent Merger模块（3层Transformer，对文档隐向量做排列不变融合，输出残差叠加到隐向量均值上，带RMS缩放保证量级匹配）；冻结LoRA生成头将合并后隐向量解码为单个固定秩LoRA
- 训练采用KL散度蒸馏目标，对齐合并后LoRA的输出分布与单文档Oracle LoRA的输出分布，全程冻结基座LLM和超网络，仅训练融合模块
### 关键实验结果
在SQuAD、MS MARCO、2WikiMultihopQA数据集测试，对比权重平均、SVD压缩、TIES、DARE、秩拼接等基线：
- D2L场景N=10文档合并时，SQuAD F1达21.0，较SVD压缩高5.5、较隐向量平均高2.4；MS MARCO F1达22.2，较基线高1-2个点
- SHINE场景N=10文档合并时，SQuAD F1达30.2，较权重空间方法高6-7个点；N=20时完整隐空间融合路径仅耗时0.77ms（D2L），较SVD压缩快2个数量级
> 最值得记住的结论：超网络生成的LoRA不是普通低秩权重更新，而是共享生成器诱导的适配器流形上的解码点，隐空间融合效果远优于权重/因子空间融合
