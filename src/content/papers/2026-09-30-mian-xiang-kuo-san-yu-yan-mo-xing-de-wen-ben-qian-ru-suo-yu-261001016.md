---
title: Scaling and Distilling Text Embeddings for Better Diffusibility
title_zh: 面向扩散语言模型的文本嵌入缩放与蒸馏优化
authors:
- Zekai Zhang
- Yunjie Tian
- Yanjin He
- Xiaoyan Zhang
- Dongdi Zhao
- Qing Qu
- Di Fu
affiliations:
- University of Michigan
arxiv_id: '2610.01016'
url: https://arxiv.org/abs/2610.01016
pdf_url: https://arxiv.org/pdf/2610.01016
published: '2026-09-30'
collected: '2026-10-02'
category: LLM
direction: 扩散语言模型 · 嵌入空间优化
tags:
- diffusion-language-model
- text-embedding
- knowledge-distillation
- latent-space
- diffusibility
one_liner: 通过嵌入模型缩放与软标签蒸馏，为连续扩散语言模型构建高可扩散性文本嵌入空间
practical_value: '- 做生成式推荐/电商文案生成的扩散模型时，可优先选用同家族更强的预训练嵌入作为基线，无需修改扩散架构即可获得约40%的Gen.PPL下降，投入成本低收益明显

  - 若遇到生成内容不稳定、无效解码多的问题，可借鉴软标签蒸馏思路：用大模型解码器输出的概率分布作为软标签训练小嵌入编码器，拉近语义相近候选的嵌入距离，可将无效嵌入占比降低90%左右

  - 设计Item Semantic ID/用户兴趣嵌入时，如果后续要接生成/匹配模块，可适当权衡判别性和生成友好性，拉近相似Item/兴趣的嵌入距离，提升下游生成/匹配的鲁棒性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
连续扩散语言模型（DLM）相比自回归生成并行度更高、可控性更强，但核心瓶颈是文本嵌入空间的可扩散性不足：现有强预训练嵌入判别性过高，语义相近候选的嵌入过度分离，采样稍有偏差就会落到无效嵌入区域，解码出错率高，此前没有针对DLM优化嵌入空间的系统落地方案。
### 方法关键点
- 固定DLM框架为ELF，仅替换嵌入模块，验证同家族嵌入模型缩放（T5-small→T5Gemma-1→T5Gemma-2）可直接提升可扩散性，无需修改扩散模型架构
- 针对强嵌入的过度分离问题，采用软标签蒸馏方案：以T5Gemma-2为教师，学生编码器学习教师解码器输出的token概率分布作为软标签，拉近语义相近候选的嵌入距离，同时保留编解码能力
- 蒸馏时仅训练学生编码器，教师模块全程冻结，蒸馏后的学生编码器参数仅为教师的一半，编码速度提升近1倍
### 关键结果
- 数据集采用OpenWebText、LM1B，对比基线包括GPT-2-S/M、ELF原生T5-small、各类SOTA连续/离散DLM
- 缩放后的T5Gemma-2嵌入相比T5-small在同熵下Gen.PPL下降40%；蒸馏后的学生嵌入配合ELF-M模型，在OpenWebText上达到Gen.PPL 17.8（接近真实文本的15.4），优于GPT-2-M的20.8
- 每1024token序列的无效嵌入数量从T5Gemma-2的109个降至12个，低NFE采样稳定性大幅提升
### 核心结论
文本嵌入的判别性和生成友好性存在天然权衡，适合扩散生成的嵌入空间不需要每个语义都过度区分，而是要让相似语义的嵌入形成连续连通区域，降低采样容错成本
